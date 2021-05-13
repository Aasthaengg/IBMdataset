import sys

n,m=map(int,raw_input().split())
list1 = [[0 for i in range(m)]for i in range(n)]
list2 = [[0 for i in range(1)]for i in range(m)]
list3 = [[0 for i in range(1)]for i in range(n)]
for i in range(n):
	list1[i] = map(int,raw_input().split())
for i in range(m):
	list2[i] = map(int,raw_input().split())
for i in range(n):
	for j in range(1):
		for k in range(m):
			list3[i][j] += list1[i][k] * list2[k][j]
for i in range(n):
	for j in range(1):
			print'%d' %list3[i][j]