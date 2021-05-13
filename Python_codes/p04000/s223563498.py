"""
l = input().split(" ")
w = int(l[0])
h = int(l[1])
n = int(l[2])

array = [[0 for i in range(h)] for j in range(w)]

for i in range(n):
	l = input().split(" ")
	x = int(l[0]) - 1
	y = int(l[1]) - 1
	for i in range(3):
		for j in range(3):
			if x+j-1 >=0 and x+j-1<w and y+i-1 >=0 and y+i-1<h:
				array[x+j-1][y+i-1] += 1

ans = [0 for i in range(10)]

for i in range(h-2):
	for j in range(w-2):
		ans[array[j+1][i+1]] += 1

for a in ans:
	print(a)

"""

l = input().split(" ")
w = int(l[0])
h = int(l[1])
n = int(l[2])

array = dict()

for i in range(n):
	l = input().split(" ")
	x = int(l[0])
	y = int(l[1])
	for i in range(3):
		if y-i < 1 or y-i > h-2:
			continue
		for j in range(3):
			if x-j < 1 or x-j > w-2:
				continue
			if (x-j, y-i) in array:
				array[(x-j, y-i)] +=1
			else:
				array[(x-j, y-i)] = 1

ans = [0] * 10
ans[0] = (h-2) * (w-2)
 
for i in array:
    ans[array[i]] += 1
    ans[0] -= 1

for i in range(10):
    print(ans[i])