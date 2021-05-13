import sys
sys.setrecursionlimit(10**9)

def dfs(x): #グラフでの再帰DFS
    if dp[x] != -1:
        return dp[x] #すでに値が決まっていたらそれをかえす
    ans = 0
    for e in graph[x]: #すべての枝について
        ans = max(ans,1 + dfs(e))
    dp[x] = ans
    return ans # 最も長い距離を返す　

n,m = list(map(int, input().split()))

graph = [[] for i in range(n+1)]
dp = [-1]
for i in range(1,n+1):
    dp.append(-1) # dpは初期値-1

for _ in range(m): # グラフの作成
    a,b = map(int, input().split())
    graph[a].append(b)
    #graph[b].append(a) #無向グラフの時
    
ans=0

for i in range(1,n+1):
    ans=max(ans,dfs(i))
print(ans)