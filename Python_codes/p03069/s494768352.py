import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    black, white = [0] * n, [0] * n
    for i in range(n):
        if s[i] == "#":
            black[i] = 1
        else:
            white[i] = 1

    acc_b = [0] + list(accumulate(black))
    acc_w = [0] + list(accumulate(white))

    res = f_inf
    for left in range(n + 1):
        change_w = acc_b[left]
        change_b = acc_w[n] - acc_w[left]
        res = min(res, change_w + change_b)
    print(res)


if __name__ == '__main__':
    resolve()
