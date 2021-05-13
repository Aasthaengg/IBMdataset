def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

import sys
input = sys.stdin.readline
n,m,r = map(int,input().split())
R = [int(i)-1 for i in input().split()]
d = [[10**9]*n for i in range(n)]
for i in range(m):
    x,y,z = map(int,input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(n):
    d[i][i] = 0
    
chk = tuple(warshall_floyd(d))
ans = float('inf')

import itertools
for i in itertools.permutations(R, r):
  p = 0
  for j in range(r-1):
    p += d[i[j]][i[j+1]]
  ans = min(ans,p)
  
print(ans) 