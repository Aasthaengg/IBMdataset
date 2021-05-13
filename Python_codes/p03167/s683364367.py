MOD = 10**9 + 7
def solve(h, w, a):
    dp = [[0]*(w+1) for y in range(h+1)]
    dp[0][0] = 1
    for y in range(h):
        for x in range(w):
            if a[y][x] == ".":
                dp[y+1][x] = (dp[y+1][x] + dp[y][x]) % MOD
                dp[y][x+1] = (dp[y][x+1] + dp[y][x]) % MOD
    return dp[h-1][w-1]

h, w = map(int, input().split())
a = [input() for y in range(h)]
print(solve(h, w, a))