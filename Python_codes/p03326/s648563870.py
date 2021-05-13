def main():
    from collections import namedtuple
    from itertools import product
    from operator import mul
    import sys
    input = sys.stdin.readline

    Cake = namedtuple('Cake', 'x y z')

    N, M = map(int, input().split())

    cakes = [Cake(*map(int, input().split())) for _ in range(N)]

    ans = 0
    for signs in product([-1, 1], repeat=3):
        e = []
        for c in cakes:
            e.append(sum(map(mul, c, signs)))
        e.sort(reverse=True)
        ans = max(ans, sum(e[:M]))

    print(ans)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()
#
# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
