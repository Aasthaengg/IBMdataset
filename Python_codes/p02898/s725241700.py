#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    _, K = map(int, readline().split())
    hs = map(int, readline().split())

    print(sum([h >= K for h in hs]))


if __name__ == '__main__':
    main()
