from collections import defaultdict as d
N,M=map(int,input().split())
E=d(int)
for i in range(M):
  a,b=map(int,input().split())
  E[a]^=1
  E[b]^=1
print(("YES","NO")[max(E.values())])