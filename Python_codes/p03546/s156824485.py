N,M=list(map(int,input().split()))
l=[list(map(int,input().split())) for i in range(10)]
s=[list(map(int,input().split())) for i in range(N)]
from scipy.sparse.csgraph import floyd_warshall
l=floyd_warshall(l)
ans=0
for i in s:
   for j in i:
      ans+=0 if j == -1 else l[j][1]
print(int(ans))