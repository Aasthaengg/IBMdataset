import sys

n,m,l=map(int,raw_input().split())
list1 = [[0 for i in range(m)]for i in range(n)]
list2 = [[0 for i in range(l)]for i in range(m)]
list3 = [[0 for i in range(l)]for i in range(n)]
for i in range(n):
	list1[i] = map(int,raw_input().split())
for i in range(m):
	list2[i] = map(int,raw_input().split())
for i in range(n):
	for j in range(l):
		for k in range(m):
			list3[i][j] += list1[i][k] * list2[k][j]
for i in range(n):
	for j in range(l):
		if j==l-1:
			print'%d' %list3[i][j]
		else:
			sys.stdout.write(str(list3[i][j]))
			sys.stdout.write(' ')