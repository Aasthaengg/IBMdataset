import sys

input = sys.stdin.readline

mod = 998244353

n, k = map(int, input().split())

lr = [list(map(int, input().split())) for _ in range(k)]
lr.sort()

if lr[0][0] == 1:
    f = [1, 1]
else:
    f = [1, 0]

for i in range(2, n):
    next_f = f[i - 1]
    for l, r in lr:
        if i - l >= 0:
            next_f += f[i - l]
        else:
            break
        if i - r - 1 >= 0:
            next_f -= f[i - r - 1]
        else:
            break
    f.append(next_f % mod)


print(f[n - 1])
