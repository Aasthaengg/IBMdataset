N = list(input())
Y = [0]
for i in N:
    Y.append(int(i))
dp = [0 for i in range(len(N)+1)]
dp2 = [10 for i in range(len(N)+1)]
for i in range(1,len(N)+1):
    dp[i] = min(dp[i-1] + Y[i],dp2[i-1] + Y[i])
    dp2[i] = min(dp[i-1] + 1 + 10 - Y[i],dp2[i-1] - 1 + 10 - Y[i])
    #print(str(dp[i])+":" +str(dp2[i]))
ans = min(dp[-1],dp2[-1])
#print(dp,dp2)
print(ans)