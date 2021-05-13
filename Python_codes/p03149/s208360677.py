#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = sorted(list(map(int, input().split())))
    if N == [1,4,7,9]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
