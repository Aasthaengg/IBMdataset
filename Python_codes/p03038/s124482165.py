n,m=map(int,input().split())
a=list(map(int,input().split()))
d=[]
ans=0
for i in range(n):
  d.append([a[i],1])
for i in range(m):
  b,c=map(int,input().split())
  d.append([c,b])
d.sort(reverse=True)
for i in range(n+m):
  if n==0:
    break
  ans+=d[i][0]*min(n,d[i][1])
  n-=min(n,d[i][1])
print(ans)