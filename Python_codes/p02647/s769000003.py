# C - Lamps

n, k = map(int, input().split())
a = list(map(int, input().split()))
assert len(a) == n

b = [0] * n
for kk in range(k):
    l = [i - a[i] for i in range(n)]
    r = [i + a[i] for i in range(n)]
    l.sort()
    r.sort()
    ln = 0
    rn = 0
    for i in range(n):
        while ln < n and l[ln] <= i:
            ln += 1
        while rn < n and r[rn] <  i:
            rn += 1
        b[i] = ln - rn
    a, b = b, a
    if all(v >= n for v in a):
        break

print(' '.join(map(str, a)))
