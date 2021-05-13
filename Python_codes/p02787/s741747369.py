H, N = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

dpl = H+max(A)
x = 10**10
dp = [x]*dpl
dp[0] = 0

for a, b in zip(A, B):
    for i in range(a, dpl):
        dp[i] = min(dp[i-a]+b, dp[i])
    for i in range(dpl-2, -1, -1):
        dp[i] = min(dp[i+1], dp[i])

print(dp[H])