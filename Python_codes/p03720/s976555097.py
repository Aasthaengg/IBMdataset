n,m=map(int,input().split())
city=[0]*n
for _ in range(m):
	a,b=map(int,input().split())
	a,b=a-1,b-1
	city[a]+=1
	city[b]+=1
for i in city:
	print(i)