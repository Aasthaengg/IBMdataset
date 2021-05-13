from collections import defaultdict
n=int(input())
mod=10**9+7
d=defaultdict(int)
for i in range(2,n+1):
  c=i
  for j in range(2,c+1):
    if c%j==0:
      cnt=0
      while c%j==0:
        cnt+=1
        c//=j
      d[j]+=cnt
ans=1
for v in d.values():
  ans=(ans*(v+1))%mod
print(ans)