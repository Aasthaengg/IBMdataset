N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [False for _ in range(K+1)]
dp[0] = False
for i in range(1, K+1):
    for a in A:
        if i - a >= 0:
            if not dp[i-a]:
                dp[i] = True
                break
if dp[K]:
    print("First")
else:
    print("Second")
