import heapq
from operator import sub, add
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def eval_cake(cake):
    res = 0
    for i in range(3):
        res += abs(cake[i])
    return res


def merge_cake(a, b):
    cake = [None, None, None]
    for i in range(3):
        cake[i] = a[i] + b[i]
    return tuple(cake)


def main():
    n, m = [int(i) for i in input().strip().split()]
    cakes = [tuple([int(i) for i in input().strip().split()]) for _ in range(n)]
    candidates = []
    for i in range(8):
        ops = [None, None, None]
        for j in range(3):
            if i >> j & 1:
                ops[j] = add
            else:
                ops[j] = sub

        hq = []

        for a, b, c in cakes:
            res = 0
            res = ops[0](res, a)
            res = ops[1](res, b)
            res = ops[2](res, c)
            heapq.heappush(hq, -res)
        ans = 0
        for _ in range(m):
            ans += -1 * heapq.heappop(hq)
        candidates.append(ans)
    print(max(candidates))
    return


if __name__ == "__main__":
    main()
