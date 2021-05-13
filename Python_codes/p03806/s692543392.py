# https://abc054.contest.atcoder.jp/tasks/abc054_d

N, Ma, Mb = map(int, input().split())
la, lb, lc = [], [], []
for _ in range(N):
    ai, bi, ci = map(int, input().split())
    la.append(ai)
    lb.append(bi)
    lc.append(ci)

sumA = sum(la)
sumB = sum(lb)

Inf = int(1e10)

dp = [[[Inf for _ in range(sumB + 1)] for _ in range(sumA + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0


for i in range(1, N + 1):
    ai, bi, ci = la[i - 1], lb[i - 1], lc[i - 1]

    for j in range(sumA + 1):
        for k in range(sumB + 1):
            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
            if j - ai >= 0 and k - bi >= 0 and dp[i - 1][j - ai][k - bi] != Inf:
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - ai][k - bi] + ci)

ans = Inf
for j in range(1, sumA + 1):
    for k in range(1, sumB + 1):
        if Mb * j == Ma * k:
            ans = min(ans, dp[N][j][k])
if ans == Inf:
    print(-1)
else:
    print(ans)