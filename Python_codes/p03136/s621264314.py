#!/usr/bin/env python3
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    l = list(map(int, input().split()))
    if max(l) < sum(l) - max(l):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
