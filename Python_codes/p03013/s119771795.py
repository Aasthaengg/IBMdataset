import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
 
n, m = map(int, readline().split())
a = set(map(int, read().split()))
 
dp = [0] * (n + 1)
dp[0] = 1
if 1 not in a:
    dp[1] = 1
cnt = 0
for i in range(2, n + 1):
    if i not in a:
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        cnt = 0
    else:
        cnt += 1
        if cnt == 2:
            print('0')
            exit()
print(dp[n])