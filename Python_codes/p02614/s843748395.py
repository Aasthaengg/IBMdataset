
from itertools import combinations

H , W , K = map(int, input().split())
C = []

for i in range(H):
	C.append(input())#C[i-1][j-1]でi行j列指定できる。

count = 0
Count = 0


#行、列いずれも1~H-1,W-1個選ぶ。
for k in range(1,H):
	for l in range(1,W):
		for i in combinations(list(range(1,H+1)),k):
			for j in combinations(list(range(1,W+1)),l):		
				count = 0
				for m in range(1,H+1):
					for n in range(1,W+1):
						if not(m in i) and not(n in j) and C[m-1][n-1] == '#':
							count += 1
				if K == count:
					Count += 1

#行のみ選ぶ、
for k in range(1,H):
	for i in combinations(list(range(1,H+1)),k):
		count =0
		for m in range(1,H+1):
			for n in range(1,W+1):
				if not(m in i) and C[m-1][n-1] == '#':
					count += 1
		if K == count:
			Count += 1

#列のみ選ぶ。
for l in range(1,W):
	for j in combinations(list(range(1,W+1)),l):
		count = 0
		for m in range(1,H+1):
			for n in range(1,W+1):
				if not(n in j) and C[m-1][n-1] == '#':
					count += 1
		if K == count:
			Count += 1


#一つも選ばない
count = 0 
for m in range(1,H+1):
	for n in range(1,W+1):
		if C[m-1][n-1] == '#':
			count += 1
if K == count:
	Count += 1





print(Count)
						


