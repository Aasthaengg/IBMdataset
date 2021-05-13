n=int(input())
m=10
f=[list(map(int,input().split())) for _ in range(n)]
p=[list(map(int,input().split())) for _ in range(n)]
ans=-10**18
for i in range(1,2**m):
  s=0
  for j in range(n):
    cnt=0
    for k in range(m):
      if (i>>k)&1 and f[j][k]:
        cnt+=1
    s+=p[j][cnt]
  ans=max(s,ans)
print(ans)