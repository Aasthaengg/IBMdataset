#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    X, Y = map(int, input().split())

    ans = 0
    if X == 3:
        ans += 100000
    if Y == 3:
        ans += 100000
    if X == 2:
        ans += 200000
    if Y == 2:
        ans += 200000
    if X == 1:
        ans += 300000
    if Y == 1:
        ans += 300000
    if X == 1 and Y == 1:
        ans += 400000

    print(ans)

if __name__ == '__main__':
    main()
