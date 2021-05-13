n,m,q = map(int,input().split())

lr = [[0 for i in range(n+1)] for j in range(n+1)]


for i in range(m):
    l,r = map(int,input().split())
    lr[l][r] += 1

pq = [[int(i) for i in input().split()]for j in range(q)]

dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(i,n+1):
        dp[i][j] = dp[i][j-1]+lr[i][j]

ans_dp = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(i,n+1):
        tmp = 0
        for k in range(j-i+1):
            tmp += dp[i+k][j]
        ans_dp[i][j] = tmp

for i in range(q):
    print(ans_dp[pq[i][0]][pq[i][1]])
