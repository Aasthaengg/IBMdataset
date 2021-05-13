INF = 10**9

N, M = map(int, input().split())
key = []
for _ in range(M):
    ab = list(map(int, input().split()))
    box = list(map(int, input().split()))
    index = sum(list(map(lambda x:2**(x-1), box)))
    ab.append(index)
    key.append(ab)
dp = [[key[0][0] if (i & ~key[0][2]) == 0 else INF for i in range(2**N)]]
dp[0][0] = 0
for j in range(1, M):
    next = [0 for _ in range(2**N)]
    for i in range(2**N):
        next[i] = min(dp[j-1][i], dp[j-1][(i & ~key[j][2])]+key[j][0])
    dp.append(next)
if dp[-1][-1] > 10**7:
    print(-1)
else:
    print(dp[-1][-1])

