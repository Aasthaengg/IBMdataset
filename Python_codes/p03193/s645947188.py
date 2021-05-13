#coding:utf-8

n = list(map(int,input().split()))
alist = [list(map(int,input().split())) for i in range(n[0])]

res = 0

for i in range(n[0]):
	if n[1] <= alist[i][0] and n[2] <= alist[i][1]:
		res += 1
		
print(res)