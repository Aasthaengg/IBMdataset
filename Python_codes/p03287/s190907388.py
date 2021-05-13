import collections
import math
N,M=map(int,input().split())
A=list(map(int,input().split()))
F_a=[]
count=0
for a in A:
  count+=a
  count%=M
  F_a.append(count)
F = collections.Counter(F_a)
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
ans=F[0]
for f in F.values():
  if f>=2:
    ans+=combinations_count(f, 2)
print(ans)