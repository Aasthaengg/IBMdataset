#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    A, B, C, K = map(int, input().split())

    if K <= A:
        print(K)
    elif K <= A + B:
        print(A)
    else:
        print(A - (K - A - B))


if __name__ == '__main__':
    main()
