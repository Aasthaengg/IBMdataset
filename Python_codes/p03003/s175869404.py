n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
q = 10**9 + 7

dp = [[None] * m for _ in range(n)] #[i][j]: s[i], t[j]を使ってできる部分列の数
sumdp = [[None] * m for _ in range(n)]

if s[0] == t[0]:
    dp[0][0] = 1
    sumdp[0][0] = 2
else:
    dp[0][0] = 0
    sumdp[0][0] = 1
    
# j=0
for i in range(1, n):
    if s[i] == t[0]:
        dp[i][0] = 1
        #dp[i][j] = sumdp[i-1][j-1] or 0
        sumdp[i][0] = sumdp[i-1][0] + 1
        sumdp[i][0] %= q
        #sumdp[i][j] = dp[i][j] + (sumdp[i-1][j] - sumdp[i-1][j-1])
        #              + (sum[i][j-1] - sumdp[i-1][j-1]) + sumdp[i-1][j-1]
        
    else:
        dp[i][0] = 0
        sumdp[i][0] = sumdp[i-1][0]
        
for j in range(1, m):
    if s[0] == t[j]:
        dp[0][j] = 1
        sumdp[0][j] = sumdp[0][j-1] + 1
        sumdp[0][j] %= q
    else:
        dp[0][j] = 0
        sumdp[0][j] = sumdp[0][j-1]
        
for i in range(1, n):
    for j in range(1, m):
        if s[i] == t[j]:
            dp[i][j] = sumdp[i-1][j-1]
        else:
            dp[i][j] = 0
        sumdp[i][j] = dp[i][j] + sumdp[i-1][j] + sumdp[i][j-1] - sumdp[i-1][j-1]
        sumdp[i][j] %= q

print(sumdp[n-1][m-1])