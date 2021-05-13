#!/usr/bin/env python3
import sys
import fractions

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    A, B = map(int, readline().split())
    print(A * B // fractions.gcd(A, B))


if __name__ == '__main__':
    main()
