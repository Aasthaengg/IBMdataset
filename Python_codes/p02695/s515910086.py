#!/usr/bin/env python3

def main():
    import sys

    def calc(A: list):
        score = 0
        for a, b, c, d in lst:
            if A[b - 1] - A[a - 1] == c:
                score += d
        return score

    def dfs(A: list):
        nonlocal ans
        if len(A) == N:
            ans = max(ans, calc(A))
        elif len(A) == 0:
            for nx in range(1, M + 1):
                dfs(A + [nx])
        else:
            for nx in range(A[-1], M + 1):
                dfs(A + [nx])

    input = sys.stdin.readline

    N, M, Q = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(Q)]
    ans = 0
    dfs([])
    print(ans)


main()
