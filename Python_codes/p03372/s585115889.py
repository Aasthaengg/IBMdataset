import sys
input = sys.stdin.readline

n, c = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(max(sushi[0][1]-sushi[0][0], sushi[0][1]-(c-sushi[0][0]), 0))
    exit()

x = []
for i in range(n):
    x.append(sushi[i][0])

vcum = []
v = 0
for i in range(n):
    v += sushi[i][1]
    vcum.append(v)

ans = 0

# 1. 時計回りのみ（方向変換なし）
for i in range(n):
    if ans < vcum[i] - x[i]:
        ans = vcum[i] - x[i]


# 2. 反時計回りのみ（方向転換なし）
for i in range(n):
    if i == 0:
        if ans < vcum[n-1] - (c - x[0]):
            ans = vcum[n-1] - (c - x[0])
    else:
        if ans < (vcum[n - 1] - vcum[i - 1]) - (c - x[i]):
            ans = (vcum[n - 1] - vcum[i - 1]) - (c - x[i])


# 3. 時計回りのあと、方向変換して反時計回り
# right_dp[i]: 反時計回りに見て n-1~i番目 (0-index)までの寿司を取れる時(必ずしもi番目を取らなくて良い)の、カロリーの正味の最大値
right_dp = [0] * n
right_dp[n-1] = vcum[n-1] - vcum[n-2] - (c - x[n-1])
for i in reversed(range(1, n-1)):
    right_dp[i] = max(right_dp[i+1], vcum[n-1] - vcum[i-1] - (c - x[i]))

# 時計回りにi番目まで見てから折り返す(すると、反時計回りに回る時に得る正味のカロリーの最大値はright_dp[i+1]となる
for i in range(n-1):
    cal = vcum[i] - 2 * x[i] + right_dp[i+1]
    if ans < cal:
        ans = cal

# 4. 反時計回りのあと、方向変換して時計回り
# left_dp[i]: 時計回りにみてi番目(0-index)までの寿司を取れる時（必ずしもi番目を取らなくて良い）の、カロリーの正味の最大値
left_dp = [0] * n
left_dp[0] = vcum[0] - x[0]
for i in range(1, n):
    left_dp[i] = max(left_dp[i-1], vcum[i] - x[i])

# 反時計回りにi番目まで見てから折り返す (すると、時計回りに回る時に得る正味のカロリーの最大値はleft_dp[i-1]となる)
for i in range(1, n):
    cal = vcum[n-1] - vcum[i-1] - 2 * (c - x[i]) + left_dp[i-1]
    if ans < cal:
        ans = cal


print(ans)
