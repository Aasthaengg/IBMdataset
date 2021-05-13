n,m = map(int,input().split())
dp = []
key = []
for i in range(m):
    d = [10**15]*(2**n)
    d[0] = 0
    dp.append(d)
for i in range(m):
    cost,num = map(int,input().split())
    if num == 1:
        t = int(input())
        key.append([cost,2**(t-1)])
    else:
        p = list(map(int,input().split()))
        cur = 0
        for i in range(len(p)):
            cur += 2**(p[i]-1)
        key.append([cost,cur])
for i in range(m):
    for j in range(2**n):
        if i != 0:
            dp[i][j] = min(dp[i][j],dp[i-1][j])
        dp[i][j|key[i][1]] = min(dp[i][j|key[i][1]],dp[i][j]+key[i][0])
if dp[m-1][2**n-1] != 10**15:
    print(dp[m-1][2**n-1])
else:
    print(-1)
