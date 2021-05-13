N = int(input())
As = list(map(int, input().split()))
mod = 10**9+7

dp = [[0]*3 for _ in range(N+1)]
ans = 1
for i in range(N):
    a = As[i]
    dplis = dp[i]
    cnt = 0
    dp[i+1] = dplis[:]
    for j, d in enumerate(dplis):
        if a==d:
            cnt += 1
            if cnt==1:
                dp[i+1][j] = a+1
    if cnt==0:
        print(0)
        break
    ans = ans*cnt%mod
else:
    print(ans%mod)