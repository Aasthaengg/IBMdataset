H, N, *AB = map(int, open(0).read().split())
A = []
B = []
for a, b in zip(*[iter(AB)] * 2):
    A.append(a)
    B.append(b)

dp = [float("inf")] * (H + 1)
dp[0] = 0

for i in range(N):
    for h in range(H):
        dec_health = min(h + A[i], H)
        dp[dec_health] = min(dp[dec_health], dp[h] + B[i])
print(dp[-1])

