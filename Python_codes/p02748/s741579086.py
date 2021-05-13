#!/usr/bin/env python3


def main():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_cost = min(a) + min(b)
    for i in range(M):
        x, y, c = map(int, input().split())
        cost = a[x - 1] + b[y - 1] - c
        if min_cost > cost:
            min_cost = cost

    print(min_cost)


if __name__ == "__main__":
    main()
