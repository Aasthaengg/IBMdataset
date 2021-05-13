N, ma, mb = map(int, input().split())
abc = [(-1, -1, -1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    abc.append((a, b, c))

INF = float("inf")

# dp[n][i][j] :=
# n番目までの薬品の組み合わせで、Aがiグラム, 物質Bがjグラムとなる溶液の最小コスト
# N <= 40, a,b <= 10 なので、 i,j <= 400
dp = [[[INF for _ in range(401)] for _ in range(401)] for _ in range(N + 1)]
dp[0][0][0] = 0

for n in range(1, N + 1):
    a, b, c = abc[n]
    for i in range(401):
        for j in range(401):
            # n番目を買うことが出来る場合(=遷移元が存在する場合)
            # 買わない or 買う
            if i >= a and j >= b:
                dp[n][i][j] = min(dp[n - 1][i][j], dp[n - 1][i - a][j - b] + c)
            # n番目を買うことが出来ない場合(=遷移元が存在しない場合)
            else:
                dp[n][i][j] = dp[n - 1][i][j]

ans = INF
# i == j == 0　は不適、1から始める
for i in range(1, 401):
    for j in range(1, 401):
        # i : j = ma : mb を満たしているかどうか
        if i * mb == j * ma:
            ans = min(ans, dp[N][i][j])

if ans != INF:
    print(ans)
else:
    print(-1)
