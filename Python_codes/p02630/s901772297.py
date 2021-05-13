#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    _ = int(input())
    lst = [0 for _ in [0] * (10 ** 5 + 1)]
    sum_lst = 0
    for a in [int(x) for x in input().split()]:
        sum_lst += a
        lst[a] += 1
    Q = int(input())

    for _ in range(Q):
        B, C = map(int, input().split())

        sum_lst += (C - B) * lst[B]
        print(sum_lst)
        lst[C] += lst[B]
        lst[B] = 0


if __name__ == '__main__':
    main()
