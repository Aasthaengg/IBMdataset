import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

s = readline().rstrip().decode()
mod = 10 ** 9 + 7
ans = [0] * 13
ans[0] = 1
for check in s:
    dp = [0] * 13
    for i in range(13):
        dp[(i * 10) % 13] = ans[i] % mod
    dp += dp
    for i in range(13):
        if check == '?':
            ans[i] = sum(dp[i + 4:i + 14])
        else:
            ans[i] = dp[i - int(check)]
print(ans[5] % mod)
