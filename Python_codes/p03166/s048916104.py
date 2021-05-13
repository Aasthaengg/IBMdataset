import collections
import sys
from functools import lru_cache
sys.setrecursionlimit(int(10**9))
n, m  = [int(i) for i in input().strip().split(' ')] 
edges = collections.defaultdict(list)
for i in range(m):
    s,d = [int(i) for i in input().strip().split(' ')]
    edges[s-1].append(d-1) 
# dp = [-1]*n
maxPath = 0 
@lru_cache(None)
def dfs(node): 
    ans = 0 
    for i in edges[node]:
        ans = max(ans,dfs(i)+1)
    return ans
 
for i in range(n):
    maxPath = max(dfs(i), maxPath) 
print(maxPath)