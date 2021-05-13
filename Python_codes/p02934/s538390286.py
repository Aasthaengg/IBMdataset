#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(readline())
    As = map(int, readline().split())
    ans = 0
    for a in As:
        ans += 1 / a
    print(1/ans)


if __name__ == '__main__':
    main()
