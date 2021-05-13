#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    _ = int(readline())
    As = list(map(int, readline().split()))
    Bs = list(map(int, readline().split()))
    Cs = list(map(int, readline().split()))

    ans = 0
    for a, a_next in zip(As, As[1:]):
        ans += Bs[a-1]
        if a_next - a == 1:
            ans += Cs[a-1]
    ans += Bs[As[-1]-1]
    print(ans)


if __name__ == '__main__':
    main()
