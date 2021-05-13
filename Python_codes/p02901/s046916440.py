"""
bitDP
dp[j] => jの二進数表記で1になっている桁数と同じ番号の宝箱を全て開けるのに必要な費用の最小値
"""

N,M = map(int,input().split())
dp = [float("INF")]*(2**N)
dp[0] = 0
for _ in range(M):
    a,b = map(int,input().split())
    C = list(map(int,input().split()))
    key = 0
    for c in C:
        key += 1 << (c-1)
    for j in range(2**N-1,-1,-1):
        dp[j|key] = min(dp[j|key],dp[j]+a)

if dp[-1] == float("INF"):
    print(-1)
else:
    print(dp[-1])

