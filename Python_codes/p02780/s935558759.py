N, K = [int(_) for _ in input().split()]

P = [int(_) for _ in input().split()]

for i in range(N):
    P[i] = int(P[i] * (1 + P[i]) / 2) / P[i]

ans = 0
tmp = 0
for i in range(N):
    tmp += P[i]
    if i < K - 1: continue
    ans = max(tmp, ans)
    tmp -= P[i - K + 1]
print(ans)
