#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    K, X = map(int, readline().split())
    print(*list(range(X - K + 1, X + K)))


if __name__ == '__main__':
    main()
