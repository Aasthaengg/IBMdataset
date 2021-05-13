#!/usr/bin/env python3
def main():
    from itertools import permutations
    from math import sqrt

    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    cnt = 0
    for can_order in permutations(xy):
        cnt += 1
        for k in range(1, N):
            xi, yi = can_order[k - 1]
            xj, yj = can_order[k]
            ans += sqrt((xi - xj) ** 2 + (yi - yj) ** 2)
    # print(ans / cnt)
    print(f'{ans / cnt:.10f}')


if __name__ == '__main__':
    main()
