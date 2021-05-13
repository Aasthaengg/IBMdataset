def divisor(i):
    cnt = 0
    y = i ** (1 / 2)
    for j in range(1, int(y) + 1):
        if i % j == 0:
            cnt += (x[j] + x[i // j])
    if y % 1 == 0:
        cnt -= x[int(y)]
    return cnt

n, k = map(int, input().split())
mod = pow(10, 9) + 7
ans = 0
x = [0] * (k + 1)
for i in range(1, k + 1):
    x[i] = i - divisor(i)
    ans += (x[i] * (pow(k // i, n, mod)) % mod)
    ans %= mod
print(ans)