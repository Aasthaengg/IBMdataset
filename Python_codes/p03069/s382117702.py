import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    b = [0] * n
    w = [0] * n
    for i in range(n):
        if s[i] == "#":
            b[i] += 1
        else:
            w[i] += 1

    b = [0] + list(accumulate(b))
    w = [0] + list(accumulate(w))
    res = f_inf
    for i in range(n + 1):
        c_b = w[-1] - w[i]
        c_w = b[i]
        res = min(res, c_b + c_w)
    print(res)


if __name__ == '__main__':
    resolve()
