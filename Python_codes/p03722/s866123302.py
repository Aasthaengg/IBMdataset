"""
頂点1から頂点Nまでのルートの途中でサイクルがあれば、無限にスコアを大きくできる。
サイクルがない場合、V-1回でNまでのスコアが求まる。
サイクルがある場合、もう一周回すと、Nまでのスコアが増えているはず。
Nのスコアが増えたらサイクル有、ということ
"""
N,M = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(M)]
dp = [-1*float("INF")]*(N+1)
dp[1] = 0

for _ in range(N-1):
    for a,b,c in edges:
        dp[b] = max(dp[b],dp[a]+c)

tmp1 = dp[N]

for _ in range(N-1):
    for a,b,c in edges:
        dp[b] = max(dp[b],dp[a]+c)

tmp2 = dp[N]
if tmp2 > tmp1:
    print("inf")
else:
    print(tmp1)