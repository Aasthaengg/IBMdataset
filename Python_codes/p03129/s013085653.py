#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, K = map(int, input().split())
    if N >= 2 * (K - 1) + 1:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
