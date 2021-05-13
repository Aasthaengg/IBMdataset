n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(1<<3):
  t=[0] *n
  for j in range(n):
    for k in range(3):
      if i&(1<<k):t[j]+=xyz[j][k]
      else:t[j]-=xyz[j][k]
  t.sort()
  ans=max(ans,sum(t[n-m:]))
print(ans)