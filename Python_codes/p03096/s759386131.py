MOD = 10**9+7

n = int(input())

dp = [0 for i in range(n+1)]

if(n == 1):
    print("1")
    exit()
if(n==2):
    print("1")
    exit()

dic = {}

ind = [0 for i in range(n+1)]

for i in range(1,n+1):
    c = int(input())
    if c in dic:
        ind[i] = dic[c][-1]
        dic[c].append(i)
    else:
        dic[c] = [i]

dp[0] , dp[1],dp[2] = 1,1,1

for i in range(3,n+1):
    dp[i] = (dp[i] + dp[i-1]) % MOD
    if(ind[i] == 0):continue
    if(ind[i] == i-1):continue
    dp[i] = (dp[i] + dp[ind[i]]) % MOD

print(dp[n])