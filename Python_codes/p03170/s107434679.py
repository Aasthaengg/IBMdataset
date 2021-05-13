N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
dp = [False for _ in range(K+1)]
for i in range(1, K+1):
    for j in a:
        if i - j >= 0:
            dp[i] = dp[i] or not dp[i - j]
        else:
            break
if dp[-1]:
    print("First")
else:
    print("Second")