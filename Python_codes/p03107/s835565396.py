#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    S = input()

    ans = min(S.count('0'), S.count('1'))
    print(ans * 2)


if __name__ == '__main__':
    main()
