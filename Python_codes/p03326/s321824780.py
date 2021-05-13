n,m = map(int, input().split())
a=[]
for i in range(n):
    a.append(tuple(map(int, input().split())))

dp = []
for i in range(m+1):
    dp.append([0 for j in range(n+1)])

def f(fn):
    global dp, a
    for i in range(1,m+1):
        for j in range(i,n+1):
            if j == i:
                dp[i][j] = sum(map(fn, a[:j]))
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1] + fn(a[j-1]))

ans = []
f(lambda x: x[0]+x[1]+x[2])
ans.append(dp[m][n])
f(lambda x: x[0]+x[1]-x[2])
ans.append(dp[m][n])
f(lambda x: x[0]-x[1]+x[2])
ans.append(dp[m][n])
f(lambda x: x[0]-x[1]-x[2])
ans.append(dp[m][n])
f(lambda x: -x[0]+x[1]+x[2])
ans.append(dp[m][n])
f(lambda x: -x[0]+x[1]-x[2])
ans.append(dp[m][n])
f(lambda x: -x[0]-x[1]+x[2])
ans.append(dp[m][n])
f(lambda x: -x[0]-x[1]-x[2])
ans.append(dp[m][n])

print(max(ans))
