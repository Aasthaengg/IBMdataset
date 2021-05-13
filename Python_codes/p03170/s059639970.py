N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [[-1,0] for i in range(K+1)]
for i in range(K+1):
    for j in range(N):
        if i+a[j]<=K:
            if dp[i+a[j]][1] == 0:
                dp[i+a[j]][0] = dp[i][0]*(-1)
                dp[i+a[j]][1] = 1
            else:
                if dp[i][0] == -1:
                    dp[i+a[j]][0] = 1 
if dp[K][0] == 1:
    print('First')
else:
    print('Second')