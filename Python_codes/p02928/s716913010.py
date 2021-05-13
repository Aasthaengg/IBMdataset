import sys
rs = lambda: sys.stdin.readline().strip()
ri = lambda: int(rs())
rs_ = lambda: [_ for _ in rs().split()]
ri_ = lambda: [int(_) for _ in rs().split()]

MOD = 10 ** 9 + 7

N, K = ri_()
A = ri_()
ans = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            if i < j:
                ans += (K * (K + 1) // 2) % MOD
            elif i > j:
                ans += (K * (K - 1) // 2) % MOD
print(ans % MOD)