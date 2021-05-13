#!/usr/bin/env python3
def main():
    from itertools import combinations
    from math import sqrt

    N = int(input())
    xy = tuple(tuple(map(int, input().split())) for _ in range(N))

    ans = 0
    for can_move in combinations(xy, 2):
        xi, yi = can_move[0]
        xj, yj = can_move[1]
        ans += sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
    print(f'{ans * 2 / N:.10f}')


if __name__ == '__main__':
    main()
