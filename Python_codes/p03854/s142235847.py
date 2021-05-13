s = input()
n = len(s)
dp = [0] * (n+1)
dp[0] = 1
for i in range(1,n+1):
    if i >= 5:
        if s[i-5:i] == "dream" or s[i-5:i] == "erase":
            dp[i] = dp[i-5]
    if i >= 6:
        if s[i-6:i] == "eraser":
            dp[i] = dp[i-6]
    if i >= 5:
        if s[i-7:i] == "dreamer":
            dp[i] = dp[i-7]
if dp[n]:
    print('YES')
else:
    print('NO')

