s = input()
mod = 10**9+7
dp = [[0]*13 for _ in range(len(s))]
t = [1]
for i in range(len(s)-1):
    t.append(t[-1]*10%13)
t.reverse()
#print(t)
if (s[0]=="?"):
    for i in range(10):
        dp[0][t[0]*i%13] = +1
else:
    dp[0][t[0]*int(s[0])%13] += 1
for i in range(1,len(s)):
    if (s[i]=="?"):
        for j in range(13):
            for k in range(10):
                dp[i][(j + t[i]*k)%13] += dp[i-1][j]
                dp[i][(j + t[i]*k)%13] %= mod
    else:
        for j in range(13):
            #print(i,j,(j + t[i]*int(s[i]))%13)
            dp[i][(j + t[i]*int(s[i]))%13] += dp[i-1][j]
            dp[i][(j + t[i]*int(s[i]))%13] %= mod             
#print(dp)
print(dp[len(s)-1][5])