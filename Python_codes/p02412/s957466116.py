#coding:utf-8

while True:
	buff = [int(x) for x in input().split()]
	n = buff[0]
	m = buff[1]
	if n==m==0:
		break
	ans=0
	for i in range(1,n-1):
		for j in range(i+1, n):
			for k in range(j+1, n+1):
				if (i+j+k)==m:
					ans+=1
	print(ans)