import bisect
INF=10**18
n,*a=map(int,input().split())
l=[int(input()) for _ in range(n)]
ans=INF
for i in range(4**n):
  x=[[] for _ in range(3)]
  for j in range(n):
    if (i>>2*j)&1 and not (i>>2*j+1)&1:x[0].append(l[j])
    if not (i>>2*j)&1 and (i>>2*j+1)&1:x[1].append(l[j])
    if (i>>2*j)&1 and (i>>2*j+1)&1:x[2].append(l[j])
  cnt=0
  for j in range(3):
    if len(x[j])==0:cnt=INF
    cnt+=(len(x[j])-1)*10+abs(sum(x[j])-a[j])
  ans=min(ans,cnt)
print(ans)