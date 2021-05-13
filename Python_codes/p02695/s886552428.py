from itertools import *
n, m, q = map(int, input().split())

a = [0] * q
b = [0] * q
c = [0] * q
d = [0] * q

for i in range(q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    a[i], b[i] = a[i] - 1, b[i] - 1

p_tmp = [0] * m
for i in range(m):
    p_tmp[i] = i

p = combinations_with_replacement(p_tmp, n)

ans = 0
for x in p:
    score = 0
    for i in range(q):
        if x[b[i]] - x[a[i]] == c[i]:
            score += d[i]

    ans = max(ans, score)

print(ans)