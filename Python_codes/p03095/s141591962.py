import collections
MOD=10**9+7
N=int(input())
S=list(input())
c = collections.Counter(S)

cnt=1
for i in c.values():
  cnt*=(i+1)
  
ans=cnt-1
print(ans%MOD)
