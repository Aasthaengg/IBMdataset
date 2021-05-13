n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
c = [0 for i in range(n)]

dp = [[0 for i in range(3)] for j in range(n)]

for t in range(n):
    x = input().split()
    a[t] = int(x[0])
    dp[t][0] = a[t]
    b[t] = int(x[1])
    dp[t][1] = b[t]
    c[t] = int(x[2])
    dp[t][2] = c[t]

#dp = [[0 for i in range(3)] for j in range(n)]

ans = 0

if a and b and c:
    #dp[0][0] = a[0]
    #dp[0][1] = b[0]
    #dp[0][2] = c[0]
    #print(dp)

    for k in range(1,n):
        for x in range(3):
            dp[k][x] = max(dp[k-1][(x+1)%3], dp[k-1][(x+2)%3]) + dp[k][x]
    #print(dp)

    for x in range(3):
        ans = max(ans, dp[n-1][x])

print(ans)