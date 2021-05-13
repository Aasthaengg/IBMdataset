#!/usr/bin/env python3
import sys
import math
INF = float("inf")


def solve(A: int, B: int):
    h = 100
    w = 99
    print(h, w)

    grid = [["."]*w for row in range(h)]

    for i in range(h//2, h):
        grid[i] = ["#"]*w

    def ij_k(k):
        row = (w-1)//2
        i = (k//row)*2+1
        j = (k % row)*2+1
        return i, j

    for k in range(B-1):
        i, j = ij_k(k)
        grid[i][j] = "#"

    for k in range(A-1):
        i, j = ij_k(k)
        grid[i+h//2][j] = "."

    for i in range(h):
        r = "".join(grid[i])
        print(r)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()
