n,m = map(int,input().split())
a = list(int(input()) for i in range(m))
a.append(0)

dp = [0] * (n+1)
b = 0
for i in range(1,n+1):
    if a[b] == i:
        b += 1
    else:
        if i != 1 and i != 2:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            if i == 1:
                dp[1] = 1
            elif i == 2 and a[0] == 1:
                dp[2] = 1
            else:
                dp[1] = 1
                dp[2] = 2
print(dp[-1] % (10 ** 9 + 7))