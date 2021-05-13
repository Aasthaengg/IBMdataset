#!/usr/bin/env python3
def main():
    import sys
    from itertools import combinations_with_replacement

    input = sys.stdin.readline

    N, M, Q = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(Q)]

    ans = 0
    for pattern in combinations_with_replacement(range(1, M + 1), N):
        res = 0
        pattern = list(pattern)
        for a, b, c, d in lst:
            if pattern[b - 1] - pattern[a - 1] == c:
                res += d
        ans = max(ans, res)

    print(ans)


main()
