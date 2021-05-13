import sys
import numpy as np

input = lambda: sys.stdin.readline().rstrip()


def solve():
    a1, a2, a3 = map(int, input().split())
    s = a1 + a2 + a3
    if s <= 21:
        print('win')
    else:
        print('bust')


if __name__ == '__main__':

    solve()
