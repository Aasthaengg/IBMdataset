h,w=map(int,input().split())
INF=float('inf')

a=[]
for _ in range(10):
  c=list(map(int,input().split()))
  a.append(c)
  
for i in range(10):
  for j in range(10):
    for k in range(10):
      a[j][k]=min(a[j][k],a[j][i]+a[i][k])


ans=0
for x in range(h):
  d=list(map(int,input().split()))
  for e in d:
    if e!=-1:
      ans+=a[e][1]
      
print(ans)

