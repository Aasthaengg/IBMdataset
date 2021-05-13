n,m,q=map(int,input().split())
abcd=[list(map(int,input().split()))  for _ in range(q)]
A=[int(i) for i in range(1,m+1)]
from itertools import combinations_with_replacement
ans=0
for l in list(combinations_with_replacement(A,n)):
  t=0
  for a,b,c,d in abcd:
    if l[b-1]-l[a-1]==c:t+=d
  ans=max(t,ans)
print(ans)
