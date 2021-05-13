def min2(x,y):
    return x if x < y else y

N, M = map(int, input().split())

large = 1<<20
dp = [large]*(1<<N + 1)
dp[0] = 0
data = []
for i in range(M):
    a, b = map(int, input().split())
    bit = 0
    for c in map(int, input().split()):
        c -= 1
        bit = bit|1<<c
    data.append((a, bit))
for i, x in enumerate(data):
    a, bit = x
    for p in range(1<<N):
        dp[p|bit] = min2(dp[p] + a, dp[p|bit])
print(dp[(1<<N)-1] if dp[(1<<N)-1] != large else -1)