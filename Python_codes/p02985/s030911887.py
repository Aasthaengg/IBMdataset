import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
MOD = 10**9 + 7

n,k = map(int,input().split())
graph = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

def dfs(now,pre):
    available_color = 0  # 子ノードに使用可能な色の数
    if pre == -1:
        available_color = k-1
    else:
        available_color = k-2
    if k < len(graph[now]):
        return 0
    res = 1
    for son in graph[now]:
        if son == pre:continue
        res *= available_color
        available_color -= 1
        res %= MOD
    for son in graph[now]:
        if son == pre:continue
        res *= dfs(son,now)
        res %= MOD

    return res

ans = (k*dfs(0,-1)) % MOD
print(ans)