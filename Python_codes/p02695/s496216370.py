n,m,q=map(int,input().split())
abcd=[list(map(int,input().split()))for _ in range(q)]
ans=0
import itertools
for i in itertools.combinations_with_replacement(list(range(m)),n):
  anss=0
  for a,b,c,d in abcd:
    if i[b-1]-i[a-1]==c:anss+=d
  ans=max(ans,anss)
print(ans)
