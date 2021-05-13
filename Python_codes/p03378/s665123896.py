n,m,x = map(int,input().split())
a = list(map(int,input().split()))

for i in range(m):
	if a[i] > x:
		if i < m - i:
			print(i)
		else:
			print(m-i)
		exit()