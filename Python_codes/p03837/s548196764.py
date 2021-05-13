#隣接する点へいく最短経路で使われないことが必要。かつ十分
n,m = map(int, input().split( ))

Ad = [[] for _ in range(n)]
for _ in range(m):
    ai,bi,ci = map(int, input().split( ))
    ai -= 1
    bi -= 1
    Ad[ai].append((bi,ci))
    Ad[bi].append((ai,ci))

dp = [[10**10 for i in range(n)] for j in range(n)]
for i in range(n):
    dp[i][i] = 0
    for b,c in Ad[i]:
        dp[i][b] = c

ans = []

for k in range(n):
    for i in range(n):
        for b,c in Ad[i]:
            if dp[i][b]>dp[i][k]+dp[k][b]:
                ans.append((i,b))
                dp[i][b] = dp[i][k]+dp[k][b]
        for j in range(n):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
ans = set(ans)
#print(ans)
print(len(ans)//2)