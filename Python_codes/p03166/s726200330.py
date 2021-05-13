import sys
 
sys.setrecursionlimit(100000)
 
N, M = map(int, input().split())
memo = [-1]*N
dic = [[] for i in range(N)]
def dfs(dic, memo, v):
    if memo[v] != -1:
        return memo[v]
    plen = 0
    for i in dic[v]:
        plen = max(plen, dfs(dic, memo, i)+1)
    memo[v] = plen
    return plen
for m in range(M):
    x, y = map(int, input().split())
    dic[x-1].append(y-1)
    
ans = 0
for i in range(N):
    ans = max(ans, dfs(dic, memo, i))
print(ans)