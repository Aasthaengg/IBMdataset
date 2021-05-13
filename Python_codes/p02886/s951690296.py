#!/usr/bin/env python3
import sys
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    _ = int(readline())
    ds = map(int, readline().split())

    ans = 0
    for d1, d2 in itertools.combinations(ds, 2):
        ans += d1 * d2
    print(ans)

if __name__ == '__main__':
    main()
