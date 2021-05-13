def solve():
    import sys
    n, m, *LR = map(int, sys.stdin.read().split())
    L = LR[::2]
    R = LR[1::2]
    l = max(L)
    r = min(R)
    print(max(0, r - l + 1))


solve()
