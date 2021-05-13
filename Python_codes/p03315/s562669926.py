#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    S=input()
    print(S.count('+')-S.count('-'))


if __name__ == '__main__':
    main()