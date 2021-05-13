from itertools import product

MAX = 10**4
N, Ma, Mb = map(int, input().split())
chems = [tuple(map(int, input().split())) for _ in range(N)]
chems = sorted(chems, key=lambda x: x[2])
rng = range(401)
dp = [[[None for _ in rng] for _ in rng] for _ in range(N+1)]
dp[0][0][0] = MAX
for i, (a, b, c) in enumerate(chems):
    for j, k in product(rng, repeat=2):
        if j < a or k < b:
            dp[i+1][j][k] = dp[i][j][k]
        else:
            if dp[i][j-a][k-b] == MAX:
                dp[i+1][j][k] = min(c, dp[i][j][k]) if dp[i][j][k] is not None else c
            elif dp[i][j-a][k-b] is not None:
                dp[i+1][j][k] = min(dp[i][j-a][k-b] + c, dp[i][j][k]) if dp[i][j][k] is not None else dp[i][j-a][k-b] + c
            else:
                dp[i+1][j][k] = dp[i][j][k]
ans = MAX
for j, k in product(rng, repeat=2):
    if j == 0 or k == 0: continue
    if j * Mb == k * Ma and dp[N][j][k] is not None:
        ans = min(ans, dp[N][j][k])
print(-1 if ans == MAX else ans)