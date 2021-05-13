import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

x, y = inm()
INF = 1 << 50


def solve():
    ans = INF
    if x < y:
        ans = min(ans, y - x)
        if x < 0 and -x <= y:
            ans = min(ans, 1 + y + x)
        if x < 0 and -x > y:
            ans = min(ans, -y - x + 1)
    elif x >= 0:
        if -y >= -x:
            ans = min(ans, 1 + (-y + x) + 1)
        if y >= -x:
            ans = min(ans, y + x + 1)
        else:
            ans = min(ans, -y - x + 1)
    else:
        ans = min(ans, -y - x + 1)
        if -y >= -x:
            ans = min(ans, -y + x + 2)

    return ans


print(solve())
