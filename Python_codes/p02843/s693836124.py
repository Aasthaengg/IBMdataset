x = int(input())
dp = [False] * (x+1)
dp[0] = 1
for i in range(0, x+1):
    if dp[i]:
        try:
            dp[i + 100] = True
            dp[i + 101] = True
            dp[i + 102] = True
            dp[i + 103] = True
            dp[i + 104] = True
            dp[i + 105] = True
        except:
            pass

if dp[x]:
    print(1)
else:
    print(0)