#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S, T = (s.decode() for s in readline().rstrip().split())
    A, B = map(int, readline().split())
    U = readline().rstrip().decode()
    if S == U:
        A -= 1
    else:
        B -= 1
    print(A, B)


if __name__ == '__main__':
    main()
