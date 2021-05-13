h, w, K = map(int, input().split())

mod = 10**9+7
dp = [[0] * w for _ in range(h+1)]
dp[0][0] = 1

for i in range(1, h+1):
    for j in range(w):
        left, center, right = 0, 0, 0

        for k in range(2**(w-1)):
            invalid = False
            for l in range(1, w-1):
                if k >> l & 1 and k >> (l-1) & 1:
                    invalid = True

            if invalid:
                continue

            no_line = True

            if j > 0:
                if k >> (j-1) & 1:
                    left += 1
                    no_line = False

            if j < w-1:
                if k >> j & 1:
                    right += 1
                    no_line = False

            if no_line:
                center += 1

        if j > 0:
            dp[i][j] += dp[i-1][j-1] * left

        if j < w-1:
            dp[i][j] += dp[i-1][j+1] * right

        dp[i][j] += dp[i-1][j] * center
        dp[i][j] %= mod

print(dp[h][K-1])
