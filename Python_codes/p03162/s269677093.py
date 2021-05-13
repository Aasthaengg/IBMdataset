n = int(input())
a = []
b = []
c = []
for i in range(n):
    ai,bi,ci = [int(x) for x in input().split()]
    a.append(ai)
    b.append(bi)
    c.append(ci)

dp = []
for i in range(n):
    dp.append([-float('inf')]*3)

dp[-1][0] = a[-1]
dp[-1][1] = b[-1]
dp[-1][2] = c[-1]

for i in range(n-2,-1,-1):
    dp[i][0] = max(dp[i+1][1],dp[i+1][2])+a[i]
    dp[i][1] = max(dp[i+1][0],dp[i+1][2])+b[i]
    dp[i][2] = max(dp[i+1][0],dp[i+1][1])+c[i]
    
print(max(dp[0][0],dp[0][1],dp[0][2]))
