n=int(input())
ans=0
c=[]
for i in range(n):
	x,y=map(int,input().split())
	ans+=x
	c.append(x+y)
c.sort()
c.reverse()
for i in range(n):
	if i%2!=0:
		ans-=c[i]
print(ans)
