import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 行列のDPを持つ　縦軸がa
N, Ma, Mb = lr()
INF = 5000
limit = N * 10 + 1
dp = [[INF] * limit for _ in range(limit)]
dp[0][0] = 0
for _ in range(N):
    a, b, c = lr()
    used = set()
    for i in range(limit):
        if i < a:
            continue
        for j in range(limit):
            if j < b:
                continue
            # 商品は１個しか買えない            
            if (i-a, j-b) not in used:
                if dp[i][j] > dp[i-a][j-b] + c:
                    used.add((i, j))
                    dp[i][j] = dp[i-a][j-b] + c

answer = INF
for i in range(1, limit):
    if i % Ma != 0:
        continue
    for j in range(1, limit):
        if j % Mb != 0:
            continue
        if i // Ma == j // Mb:
            if dp[i][j] < answer:
                answer = dp[i][j]

print(answer if answer != INF else -1)
# 10