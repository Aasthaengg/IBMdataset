# 解説参照
k = int(input())
n = len(input())

mod = 10 ** 9 + 7
f = [1] + [1]
for i in range(2, n + k + 1 + 26):
    f.append(f[-1] * i % mod)

inv = [0] + [1]
for i in range(2, n + k + 2 + 26):
    inv += [inv[mod % i] * (mod - int(mod / i)) % mod]

inv_f = [1, 1]
for i in range(2, n + k + 2 + 26):
    inv_f.append(inv_f[-1] * inv[i] % mod)


def c(x, y):
    return f[x] * inv_f[x - y] * inv_f[y]


ans = 0

for i in range(k + 1):
    ans += c(n + k - i - 1, n - 1) * pow(25,k-i,mod)*pow(26,i,mod)

print(ans % mod)