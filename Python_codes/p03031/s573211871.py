import itertools
n,m=map(int,input().split())
xs=[list(map(int,input().split()))[1:] for i in range(m)]
p=tuple(map(int,input().split()))
ans=0
for switch in itertools.product(range(2),repeat=n):
  judge=True
  for i in range(m):
    cnt=0
    lst=xs[i]
    for j in lst:
      cnt+=switch[j-1]
    if cnt%2!=p[i]:
      judge=False
      break
  if judge:
    ans+=1

print(ans)
