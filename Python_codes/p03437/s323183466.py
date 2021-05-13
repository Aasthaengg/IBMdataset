#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    X, Y = map(int, input().split())

    if X % Y == 0:
        print(-1)
        exit()

    for i in range(1, 10**8):
        num = X * i
        if num % Y != 0:
            print(num)
            exit()

if __name__ == '__main__':
    main()
