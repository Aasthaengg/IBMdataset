#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, A, B = map(int, input().split())

    MaxAns = min(A, B)
    MinAns = 0
    if N >= A + B:
        pass
    else:
        MinAns = -(N - A - B)

    print(MaxAns, MinAns)


if __name__ == '__main__':
    main()
