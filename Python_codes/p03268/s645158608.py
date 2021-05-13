N, K = [int(v) for v in input().split()]

kcnt = [0] * K

for i in range(1, N + 1):
    kcnt[i % K] += 1

ans = 0
for a in range(1, K + 1):  # aを固定
    b = K - (a % K)
    c = K - (a % K)
    if (a + b) % K == 0 and (a + c) % K == 0 and (b + c) % K == 0:
        ans += kcnt[a%K] * kcnt[b%K] * kcnt[c%K]

print(ans)