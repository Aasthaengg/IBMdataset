n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
y=[]
import bisect
for i in range(n):
	y.append(bisect.bisect_left(a,b[i]))
ans=0
q=[]
for i in range(n):
	p=bisect.bisect_left(b,c[i])
	q.append(p)
k=sum(y[0:q[0]])
for i in range(n-1):
	ans+=k
	if q[i+1]!=q[i]:
		k+=sum(y[q[i]:q[i+1]])
ans+=k
print(ans)

