import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())
g=[[] for _ in range(n)]

for i in range(n-1): # 行列の作成
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

costs = [0]*n # 答えの格納

for i in range(q): # コスト初期値の入力
    p, x = map(int, input().split())
    costs[p-1]+=x

visited = [0]*n # 訪問スタンプ

def dfs(idx):
    visited[idx]=1
    for i in g[idx]:
        if visited[i]==1:
            continue
        costs[i]+=costs[idx] # 累積和をとる
        dfs(i) # 再帰処理
    return

dfs(0)
print(*costs)
