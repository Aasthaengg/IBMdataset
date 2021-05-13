# coding: utf-8

# https://atcoder.jp/contests/abc115


def main():
    N = int(input())
    p = [None] * N
    for i in range(N):
        p[i] = int(input())
    
    p = sorted(p)
    return sum(p[:-1]) + p[-1]//2


print(main())
