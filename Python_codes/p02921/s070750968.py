#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S = readline().rstrip()
    T = readline().rstrip()
    ans = 0
    for s, t in zip(S, T):
        if s == t:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
