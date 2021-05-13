import itertools
n, m, d = map(int, raw_input().split())

def solve():
    if d >= n:
        return 0.0
    if n == 1:
        return 1.0

    k = 1.0*(m - 1)*2/n**2
    t = n/2 if d == 0 else n - d
    return k*t

print("%.15f"%solve())
