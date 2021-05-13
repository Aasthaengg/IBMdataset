#!/user/bin/env pypy3
import collections
import sys


def fast_input():
    return sys.stdin.readline()[:-1]


def solve(c_500: int, c_100: int, c_50: int, amount: int) -> int:
    amount_list = []
    for i_500 in range(c_500 + 1):
        for i_100 in range(c_100 + 1):
            for i_50 in range(c_50 + 1):
                amount_list.append(i_500 * 500 + i_100 * 100 + i_50 * 50)

    return amount_list.count(amount)


def main():
    c_500 = int(fast_input())
    c_100 = int(fast_input())
    c_50 = int(fast_input())
    amount = int(fast_input())
    result = solve(c_500, c_100, c_50, amount)
    print(result)


main()
