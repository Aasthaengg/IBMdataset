#!/usr/bin/env python3
def main():
    from itertools import permutations

    N = int(input())
    P = tuple(int(x) for x in input().split())
    Q = tuple(int(x) for x in input().split())

    for i, p in enumerate(permutations(range(1, N + 1), N)):
        if p == P:
            a = i
    for i, q in enumerate(permutations(range(1, N + 1), N)):
        if q == Q:
            b = i
    print(abs(a - b))


if __name__ == '__main__':
    main()
