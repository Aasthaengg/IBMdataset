h, w = map(int, input().split(" "))
dp = [[0 for i in range(w)] for j in range(h)]
mod=1e9+7
for i in range(h):
    s = input()
    for j in range(w):
        if i==0 and j==0:
            dp[0][0]= 1 if (s[j]=='.') else 0
        elif i==0:
            dp[0][j]= dp[0][j-1] if (s[j]=='.') else 0
        elif j==0:
            dp[i][0]= dp[i-1][0] if (s[0]=='.') else 0
        else:
            dp[i][j]= (dp[i-1][j]%mod+dp[i][j-1]%mod)%mod if s[j]=='.' else 0
print(int(dp[h-1][w-1]%mod))
