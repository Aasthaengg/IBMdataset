s = input()

if(len(s) <= 2):
    print(len(set(list(s))))
    exit()
dp = [0 for _ in range(len(s)+1)]
dp[0] = 0
dp[1] = 1
dp[2] = len(set(list(s[:2])))
for i in range(3,len(s)+1):
    if(s[i-1] != s[i-2]):dp[i] = dp[i-1] + 1
    else:dp[i] = dp[i-3] + 2
print(dp[-1])