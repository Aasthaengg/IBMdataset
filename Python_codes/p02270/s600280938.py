import sys
readline = sys.stdin.readline
n, k = map(int, input().split())
v = [int(readline()) for _ in range(n)]
lo = max(v) - 1
hi = int(1e10)
while hi - lo > 1:
    p = P = (lo + hi) // 2
    m = 1
    for i in range(n):
        if v[i] > p:
            p = P
            m += 1
        p -= v[i]
    if m <= k:
        hi = P
    else:
        lo = P
print(hi)

