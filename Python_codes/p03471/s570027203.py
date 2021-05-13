import sys
 
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))
 
n, y = inm()
not_discov = (-1, -1 , -1)
def solve():
    if y % 1000 != 0:
        print("-1 -1 -1")
    y_n = y // 1000
    for c in range(n + 1):
        b_tmp = y_n - 9 * c - n
        if b_tmp < 0 or b_tmp > 4 * n or b_tmp % 4 != 0:
            continue
        b = b_tmp // 4
        a = n - b - c
        if a < 0 or a > n:
            continue
        return c, b, a
    return not_discov

print(*solve())