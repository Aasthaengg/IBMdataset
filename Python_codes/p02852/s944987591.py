import sys
sys.setrecursionlimit(1000000000)
from itertools import count
from functools import lru_cache
from collections import defaultdict
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok
#


def main():
    N, M = mis()
    S = input()

    ans = []
    r = N
    l = max(r - M, 0)
    while r > 0:
        for i in range(l, r):
            if S[i] == '0':
                ans.append(r - i)
                r = i
                l = max(r - M, 0)
                break
        else:
            print(-1)
            return
    ans.reverse()
    print(*ans, sep=' ')


main()
