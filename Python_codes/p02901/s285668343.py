N,M = (int(x) for x in input().split())
abc = [[None] * 3 for _ in range(M)]
check = set()
for x in abc:
    x[0],x[1] = (int(x) for x in input().split())
    x[2] = list(map(int, input().split()))
    check = check | set(x[2])
if len(check) < N:
    print('-1')
else:
    a = [x[0] for x in abc]
    c = [0] * (M+1)
    dp = [[float('inf')] * pow(2,N) for _ in range(M+1)]
    for i in range(1,M+1):
        c[i] = sum(pow(2,y-1) for y in abc[i-1][2])
    for i in range(M+1):
        dp[i][0] = 0
    for i in range(1,M+1):
        for j in range(pow(2,N)):
            dp[i][j] = min(dp[i][j],dp[i-1][j])
            dp[i][j|c[i]] = min(dp[i][j|c[i]],dp[i][j]+a[i-1])
    print(dp[M][pow(2,N)-1])