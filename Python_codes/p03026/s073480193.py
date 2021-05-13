import sys
from collections import deque
from collections import defaultdict
import math
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
 
n = int(input())
g = [[]for i in range(n)]
for i in range(n-1):
        a,b=map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
c = list(map(int,input().split()))
kyo = [float("inf")] * n
def dfs(x,y,z):
  kyo[x] = y
  for i in g[x]:
    if i == z:
            continue
    dfs(i,y+1,x)
dfs(0,0,-1)
kyo2 = []
for i in range(n):
        kyo2.append([kyo[i],i])
ans = [0]*n
kyo2.sort()
kyo2 = kyo2[::-1]
c.sort()
for i in range(n):
        ans[kyo2[i][1]] = c[i]
print(sum(c)-c[-1])
print(*ans)