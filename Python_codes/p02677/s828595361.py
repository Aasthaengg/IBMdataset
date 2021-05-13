#!/usr/bin/env python3

import math


def solve(A: int, B: int, H: int, M: int):
    ra = (H + M / 60.0) / 12.0 * 2.0 * math.pi
    rb = M / 60.0 * 2.0 * math.pi
    xa = A * math.cos(ra)
    ya = A * math.sin(ra)
    xb = B * math.cos(rb)
    yb = B * math.sin(rb)
    answer = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    return answer


def main():
    A, B, H, M = map(int, input().split())
    answer = solve(A, B, H, M)
    print(answer)


if __name__ == "__main__":
    main()
