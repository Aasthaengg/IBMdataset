N,M = map(int,input().split())
broken = set()
for i in range(M):
    broken.add(int(input()))
if N == 1:
    if 1 in broken:
        print(0)
    else:
        print(1)
elif N == 2:
    if 2 in broken:
        print(0)
    elif 1 in broken:
        print(1)
    else:
        print(2)
else:
    dp = [0 for i in range(N+1)]
    if 1 not in broken:
        dp[1] = 1
    if 2 not in broken:
        dp[2] = dp[1] + 1
    for i in range(3,N+1):
        if i in broken:
            dp[i] = 0
        else:
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= 1000000007
    print(dp[N])