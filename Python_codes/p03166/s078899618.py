import sys
sys.setrecursionlimit(10**9)
 
 
N, M = map(int, input().split())
 
G = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    G[x] += [y]
# print(G)
 
dp = [-1] * (N + 1)
 
 
def func(n):
    if dp[n] != -1:
        return dp[n]
    cnt = 0
	# 先にノードが存在する場合
	# ノードが存在しない場合は、cnt=0のままforをすっ飛ばす
    for m in G[n]:
        cnt = max(cnt, func(m) + 1)
    dp[n] = cnt
    return cnt
 
 
for i in range(1, N + 1):
    func(i)
 
# print(dp)
print(max(dp))