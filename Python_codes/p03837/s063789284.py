n,m = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(m)]

dp = [[0 for _ in range(n)] for _ in range(n)]
INF = 10**18
for i in range(n):
    for j in range(n):
        if i!=j:
            dp[i][j] = INF
for a,b,t in l:
    dp[a-1][b-1] = t
    dp[b-1][a-1] = t
#print(dp)

#最短リスト
for c in range(n):
    for f in range(n):
        for la in range(n):
            dp[f][la] = min(dp[f][la] , dp[f][c] +  dp[c][la])

#各辺が何かしらの最短ルートに含まれているか
ans = 0
for a, b, t in l:
    cou = 0
    for j in range(n):
        for k in range(n):
            #jからkの最短ルートにa,bが入ってるいるか
            if dp[j][k] != dp[j][a-1] + t + dp[b-1][k]:
                cou += 1
    if cou==n**2:
        ans += 1

print(ans)
