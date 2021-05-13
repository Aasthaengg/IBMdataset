from itertools import permutations
n,m,r = map(int,input().split())
route = list(map(int,input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]
INF = 10**18
for i in range(n):
    for j in range(n):
        if i!=j:
            dp[i][j] = INF
for _ in range(m):
    a,b,c = map(int,input().split())
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
#print(dp)

#最短リスト
for chu in range(n):
    for fir in range(n):
        for la in range(n):
            dp[fir][la] = min(dp[fir][la] , dp[fir][chu] +  dp[chu][la])

ans = 10**10
for j in permutations(route, r):
    a = 0
    for q,w in zip(j[:-1], j[1:]):
        a += dp[q-1][w-1]
        
    ans = min(ans,a)
print(ans)