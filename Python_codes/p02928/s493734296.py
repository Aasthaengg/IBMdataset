N, K = map(int, input().split())
A_LIST = list(map(int, input().split()))
MOD = 10 ** 9 + 7
t = 0
tr = 0
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if A_LIST[i] > A_LIST[j]:
            t += 1
    for k in range(N):
        if A_LIST[i] > A_LIST[k]:
            tr += 1
ans += t * K % MOD
ans += tr * (K - 1) * K // 2 % MOD
print(ans % MOD)
