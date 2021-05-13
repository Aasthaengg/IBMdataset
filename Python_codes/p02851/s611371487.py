n,k=map(int,input().split())
A=[int(i) for i in input().split()]
ans=0
AA=[(A[0]-1)%k]
for i in range(1,n):
  AA.append((AA[-1]+A[i]-1)%k)
import collections
d=collections.defaultdict(int)
d[0]+=1
for i in range(n):
  if i+1==k:
    d[0]-=1
  elif i+1>=k:
    d[AA[i-k]]=max(0,d[AA[i-k]]-1)
  ans+=d[AA[i]]
  d[AA[i]]+=1
print(ans)
