import sys
from functools import reduce
from operator import mul
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def cmb(n: int, r: int):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    n, p = input_int_list()
    A = input_int_list()
    even = 0
    odd = 0
    for a in A:
        if a % 2 == 1:
            odd += 1
        else:
            even += 1

    if p == 1:
        ans = 2**even
        tmp = 0
        for i in range(1, odd + 1, 2):
            tmp += cmb(odd, i)
        print(ans * tmp)
    elif p == 0:
        ans = 2**even
        tmp = 0
        for i in range(0, odd + 1, 2):
            tmp += cmb(odd, i)
        print(ans * tmp)
    return


if __name__ == "__main__":
    main()
