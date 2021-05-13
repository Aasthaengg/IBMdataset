n = int(input())
cs = []
for i in range(n):
    cs.append(int(input()))
dp = [0] * n
last_num = [-1] * 2 * 10**5
MOD = 10**9 + 7

for i, c in enumerate(cs):
    if i == 0:
        dp[i] = 1
        last_num[c-1] += 1
        continue
    # Fisrt color
    if(last_num[c-1] == -1):
        dp[i] += dp[i-1]
    # Previous color
    elif(last_num[c-1] == i-1):
        dp[i] += dp[i-1]
    # Reversi
    else:
        dp[i] += dp[i-1]
        dp[i] += dp[last_num[c-1]]
    dp[i] %= MOD
    last_num[c-1] = i
print(dp[n-1])