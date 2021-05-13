#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N, K = map(int, input().split())

    ball = N - K
    if K == 1:
        ball = 0
    print(ball)

if __name__ == '__main__':
    main()
