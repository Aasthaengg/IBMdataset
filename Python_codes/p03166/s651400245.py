# 根付き木に対して根から最大でどれだけかかるかを使う方法

import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n, m = map(int, input().split())
co = [[] for i in range(n)] # 有効辺の向きを逆にした
for i in range(m):
    a, b = map(int, input().split())    
    co[b - 1].append(a - 1)

dp = [-1] * n

def memo(v):
    if dp[v] != -1: #更新済
        return dp[v]

    for i in co[v]:
        x = memo(i) + 1
        if x > dp[v]:
            parent[v] = i + 1
            dp[v] = x

    return max(dp[v], 0)
# 経路復元
parent = [0] * n


ans = 0
for i in range(n):
    ans = max(ans, memo(i))

print(ans)