#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(N: int, M: int):
    # N <= 10**5

    # 差が異なる組み合わせならば、N回を通して同じ組み合わせにはならない。
    # 前に奇数差、後ろに偶数差を作る
    ans = []

    if N % 2 == 0:
        # 差は偶数
        a, b = (0, N//2-1)
        # print(a, b)
        while a < b:
            ans.append((a+1, b+1))
            a += 1
            b -= 1
        # 差は奇数
        a, b = (N//2, N-2)
        while a < b:
            ans.append((a+1, b+1))
            a += 1
            b -= 1
    if N % 2 == 1:
        # 差は偶数
        a, b = (0, N//2)
        while a < b:
            ans.append((a+1, b+1))
            a += 1
            b -= 1
        # 差は奇数
        a, b = (N//2+1, N-1)
        while a < b:
            ans.append((a+1, b+1))
            a += 1
            b -= 1
    for i in range(M):
        print(*ans[i], sep=" ")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)


if __name__ == '__main__':
    main()
