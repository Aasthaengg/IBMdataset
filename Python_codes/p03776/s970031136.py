from scipy.misc import comb 
from collections import defaultdict, deque, Counter
import sys
#from scipy.special import comb
import heapq
import math

input = sys.stdin.readline

sys.setrecursionlimit(10000000)

MIN = -10 ** 9
MOD = 10 ** 9 + 7


def main():
    N, A, B = [int(a) for a in input().split()]
    V = sorted([int(a) for a in input().split()], reverse=True)

    s = sum(V[:A]) / A
    target = V[A - 1]
    if target == V[0]:
        co = V.count(target)
        t = sum(
            comb(co, c, exact=True)
            for c in range(A, min(B, co) + 1)
        )
        print(s)
        print(t)
        return

    c1 = V[:A].count(target)
    c2 = V.count(target)
    t = comb(c2, c1, exact=True)
    print(s)
    print(t)


if __name__ == '__main__':
    main()
