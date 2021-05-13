N = int(input())
A = list(map(int, input().split()))

M = 61
D1 = [0] * M

for a in A:
    k = 0
    while a > 0:
        if a & 1:
            D1[k] += 1
        a >>= 1
        k += 1

MOD = 10 ** 9 + 7
ans = 0
for k in range(M):
    d = D1[k]
    ans += d * (N - d) * pow(2, k, MOD)
    ans %= MOD

print(ans)
