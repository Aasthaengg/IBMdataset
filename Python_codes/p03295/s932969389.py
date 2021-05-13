#!/usr/bin/env python3
N, M = [int(str) for str in input().strip().split()]
ab = [[int(str) for str in input().strip().split()] for _ in range(M)]


def solve():
    ab.sort(key=lambda x: x[1])
    ans = 0
    broken = 0
    for a, b in ab:
        if a < broken:
            continue
        broken = b
        ans += 1
    print(ans)

solve()
