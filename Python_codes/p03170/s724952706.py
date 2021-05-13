N, K = list(map(int, input().split()))
A = set(map(int, input().split()))

dp = [False]*(K+1)
dp[0] = False
for i in range(K):
    if dp[i]:
        continue
    for s in A:
        if i+s <= K:
            dp[i+s] = True
# print(dp)
if dp[K]:
    print('First')
else:
    print('Second')
