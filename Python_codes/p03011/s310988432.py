from itertools import combinations

s=list(map(int,input().split()))
t=list(combinations(s,2))
ans=float('inf')
for i in t:
  ans=min(ans,sum(i))
print(ans)