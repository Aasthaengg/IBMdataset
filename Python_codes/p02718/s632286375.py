#!/usr/bin/env python3
def main():
    N, M = map(int, input().split())
    A = sorted([int(x) for x in input().split()], reverse=True)

    level = sum(A) / (4 * M)
    if A[M - 1] < level:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    main()
