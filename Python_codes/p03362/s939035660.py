import sys
import itertools

sys.setrecursionlimit(10 ** 8)
ni = lambda: int(sys.stdin.readline())
nm = lambda: map(int, sys.stdin.readline().split())
nl = lambda: list(nm())
ns = lambda: sys.stdin.readline().rstrip()


N = ni()
M = 55555


def solve():
    ans = []
    for p in range(7, M, 10):
        pr, j = True, 3
        while j * j <= p:
            if p % j == 0:
                pr = False
                break
            j += 2
        if pr:
            ans.append(p)
            if len(ans) == N:
                break
    print(*ans)


solve()
