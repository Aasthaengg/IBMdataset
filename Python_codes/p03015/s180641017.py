a = input()
s = len(a)
MOD = 10**9 + 7
dp = [0]*100010
ep = [0]*100010

dp[0] = 1

for i in range(s):
    ep[i+1]+= 3*ep[i]
    if a[i] == '1':
        dp[i+1] += 2*dp[i]
        ep[i+1] += dp[i]
    else:
        dp[i+1]+=dp[i]
    
    ep[i+1]%=MOD
    dp[i+1]%=MOD
ans = (dp[s]+ep[s])%MOD
print(ans)