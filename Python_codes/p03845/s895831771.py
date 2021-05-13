n=int(input())
c=list(map(int,input().split()))
l=int(input())
for i in range(l):
	a,b=map(int,input().split())
	temp=c[a-1]
	c[a-1]=b
	print(sum(c))
	c[a-1]=temp

