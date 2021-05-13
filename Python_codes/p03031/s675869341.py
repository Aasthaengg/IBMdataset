import itertools
n,m=map(int, input().split())
k=[list(map(int, input().split())) for i in range(m)]
p=list(map(int, input().split()))
bit=list(itertools.product([0,1], repeat=n))
ans=0
for i in bit:
  cnt=0
  for j in range(m):
    cnt2=0
    for l in range(1,k[j][0]+1):
      if i[k[j][l]-1]==1:
        cnt2+=1
    if cnt2%2==p[j]:
      cnt+=1
  if cnt==m:
    ans+=1
print(ans)