#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())
    H = list(map(int, input().split()))

    k = 0
    for i in range(N - 1):
        k += H[i + 1] - H[i]
        if k > 0:
            k = 0
        if k <= -2:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    main()
