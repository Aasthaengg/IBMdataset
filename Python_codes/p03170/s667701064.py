N, K = map(int, input().split())
a_list = list(map(int, input().split()))

dp = [False] * (K+1)
for i in range(1, K+1):
    for a in a_list:
        if i >= a:
            dp[i] = dp[i] or ~dp[i-a]
if dp[K]:
    print('First')
else:
    print('Second')