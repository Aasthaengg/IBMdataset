H, W, K = map(int, input().split())

mod = 10 ** 9 + 7


def Fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n - 2):
            a, b = b, a + b
        return b


dp = [[0 for j in range(W + 5)] for i in range(H + 5)]  # dp[h][k]
dp[0][1] = 1
for i in range(1, H + 1):
    for j in range(1, W + 1):
        for t in [-1, 0, 1]:
            if 1 <= j + t <= W:
                used = [0 for _ in range(W + 1)]
                for y in [j, j - 1, j + t, j + t - 1]:
                    if y >= 0:
                        used[y] = 1
                l = -(used[0] == 0)
                for x in used:
                    if x == 0:
                        l += 1
                    else:
                        break
                r = -(used[W] == 0)
                for x in used[::-1]:
                    if x == 0:
                        r += 1
                    else:
                        break
                dp[i][j] += Fib(l + 3) * Fib(r + 3) * dp[i - 1][j + t]
                dp[i][j] %= mod
print(dp[H][K])