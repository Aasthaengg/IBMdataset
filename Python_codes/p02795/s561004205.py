#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    H = int(input())
    W = int(input())
    N = int(input())

    ans = N // max(H, W)
    if N % max(H, W) != 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
