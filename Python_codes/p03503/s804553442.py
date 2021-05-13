n=int(input())
f=[list(map(int,input().split())) for _ in range(n)]
p=[list(map(int,input().split())) for _ in range(n)]
ans=-10**18
for i in range(1,2**10):
  idx=set()
  for j in range(10):
    if (i>>j)&1:
      idx.add(j)
  s=0
  for j in range(n):
    cnt=0
    for k in range(10):
      if k in idx:
        if f[j][k]:
          cnt+=1
    s+=p[j][cnt]
  ans=max(ans,s)
print(ans)