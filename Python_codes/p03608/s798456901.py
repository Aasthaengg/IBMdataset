import itertools

N,M,R = map(int,input().split())

r = list(map(int,input().split()))
for i in range(R):
    r[i] -= 1

inf = 10 ** 12

dp = [[inf]*N for i in range(N)]
for i in range(M):
    A,B,C = map(int,input().split())
    A -= 1
    B -= 1
    dp[A][B] = C
    dp[B][A] = C

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])

l = list(range(R))
m = inf

for x in itertools.permutations(l,R):
    count = 0
    for i in range(len(l)-1):
        count += dp[r[x[i]]][r[x[i+1]]]
    m = min(count,m)

print(m)