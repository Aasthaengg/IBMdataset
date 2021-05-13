N, K = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
Memo = [0] * (K + 1)

for i in range(1, K+1)[::-1]:
    num = K // i
    a = pow(num, N, mod)
    for j in range(2, K+1):
        if j * i > K:
            break
        a -= Memo[j * i]
    Memo[i] = a % mod
    ans += a * i
    ans %= mod

print(ans % mod)