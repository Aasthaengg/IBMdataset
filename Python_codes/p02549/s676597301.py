import sys

input = sys.stdin.readline

mod = 998244353

n, k = map(int, input().split())

lr = [list(map(int, input().split())) for _ in range(k)]
lr.sort()

a = [0] * n
a[0] = 1
a[1] = -1
f = [1]

for i in range(n - 1):
    for l, r in lr:
        if i + l < n:
            a[i + l] += f[i]
            a[i + l] %= mod
        else:
            break
        if i + r + 1 < n:
            a[i + r + 1] -= f[i]
            a[i + r + 1] %= mod
        else:
            break
    f.append((f[i] + a[i + 1]) % mod)
print(f[n - 1])
