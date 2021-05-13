n,k=map(int,input().split())
ab=[[] for i in range(n+1)]
for i in range(n-1):
  a,b=map(int,input().split())
  ab[a]+=[[b,a]]
  ab[b]+=[[a,b]]
x=k
c=[]+ab[1]
d=[0]*(n+1)
while c:
  y,z=c.pop()
  c+=[i for i in ab[y] if i[0]!=z]
  x=(x*max(0,k-1-d[z]))%(10**9+7)
  d[z]+=1
  d[y]=1
print(x)