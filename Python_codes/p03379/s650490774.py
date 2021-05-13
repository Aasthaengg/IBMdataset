from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import math

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

n = readInt()
t = readInts()
x = []
for i in range(n):
	x.append([i,t[i]])
x = sorted(x, key=lambda x: x[1])
ans = [-1]*n
for i in range(len(x)):
	if i<n//2:
		ans[x[i][0]]=x[n//2][1]
	else:
		ans[x[i][0]]=x[n//2-1][1]

for i in ans:
	print(i,end=" ")