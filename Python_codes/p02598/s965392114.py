# coding: utf-8
import numpy as np


def solve(*args: str) -> str:
    n, k = map(int, args[0].split())
    A = np.array(tuple(map(int, args[1].split())))

    l, r = 0, np.max(A)
    while l+1 < r:
        m = (l+r)//2
        if k < np.sum(np.ceil(A/m)-1):
            l = m
        else:
            r = m

    return str(r)


if __name__ == "__main__":
    print(solve(*(open(0).read().splitlines())))
