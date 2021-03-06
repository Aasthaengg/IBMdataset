# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

def prime_factorization(x):
    """素因数分解"""
    import math
    re = []
    i = 2
    while x != 1:
        if x % i == 0:
            re.append(i)
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.append(x)
                break
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    pf = []
    for i in range(1, N + 1):
        pf += prime_factorization(i)
    pf_nums = [0] * (N + 1)
    for p in pf:
        pf_nums[p] += 1

    def num(m):
        return len([i for i in pf_nums if i >= m - 1])

    ans = num(75) + \
          num(25) * (num(3) - 1) + \
          num(15) * (num(5) - 1) + \
          num(5) * (num(5) - 1) * (num(3) - 2) // 2

    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
