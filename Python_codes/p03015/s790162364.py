L = input()
Digit = len(L)
dp = [[0]*2 for _ in range(Digit+1)]
dp[0][0] = 1
mod = 10**9+7
# 配りdp
for i in range(Digit):
    next_digit = L[i]
    
    if next_digit == '0':
        # not smallからnot smallへの遷移
        dp[i+1][0] += dp[i][0]
        # not smallからsmallへの遷移はない

        # smallからsmallへの遷移
        dp[i+1][1] += (3*dp[i][1])%mod
        
    else:
        # not smallからnot smallへの遷移
        dp[i+1][0] += (2*dp[i][0])%mod
        # not smallからsmallへの遷移
        #print(dp[i][0])
        dp[i+1][1] += dp[i][0]%mod
        # smallからsmallへの遷移
        dp[i+1][1] += (3*dp[i][1])%mod
    #print(dp[i],dp[i+1])
    #print('---')

#print(dp)
print((dp[-1][1]+dp[-1][0])%mod)