import math

N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]


def check(n):
    d = n * B
    t = 0
    for h in H:
        if h <= d:
            continue
        t += (h - d + (A - B - 1)) // (A - B)
    return t <= n


lo, hi = 0, 10 ** 9

while lo < hi:
    mi = (lo + hi) // 2
    if check(mi):
        hi = mi
    else:
        lo = mi + 1

print(hi)
