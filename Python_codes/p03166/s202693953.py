import sys
sys.setrecursionlimit(10 ** 9)

n,m = map(int,input().split())
g = [[] for i in range(n)]

# xは始点、yは次点
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    
dp = [-1]*n
 
def solve(i): # 始点iから行ける場所を探索
    # すでに計算されているなら、後の距離は計算できている
    if dp[i] != -1:
        return dp[i]
    # 初期は長さ0
    tmp = 0
    # 始点iから次点にDFS
    for j in g[i]:
        #今までの距離と比較
        tmp = max(tmp, solve(j) + 1)
    # dp[i]はiからスタートして最長距離が記録される
    # 空のリスト（もう次点が存在しない）にたどり着いたらDFS終わり
    dp[i] = tmp
    return tmp
 
for i in range(n):
    solve(i)

print(max(dp))