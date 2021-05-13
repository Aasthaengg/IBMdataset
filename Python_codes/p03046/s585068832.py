# AtCoder Beginner Contest 126
# https://atcoder.jp/contests/abc126
import sys
#import numpy as np

s2nn = lambda s: [int(c) for c in s.split(' ')]
ss2nn = lambda ss: [int(s) for s in ss]
ss2nnn = lambda ss: [s2nn(s) for s in ss]
i2s = lambda: sys.stdin.readline().rstrip()
i2n = lambda: int(i2s())
i2nn = lambda: s2nn(i2s())
ii2ss = lambda n: [sys.stdin.readline().rstrip() for _ in range(n)]
ii2nn = lambda n: ss2nn(ii2ss(n))
ii2nnn = lambda n: ss2nnn(ii2ss(n))

def main():
    M, K = i2nn()
    # K = 0 のとき、a[i] == a[i+1] と連続で並べれば a[i] ^ a[i+1] == 0 より構築可能
    if K == 0:
        for i in range(2**M):
            print(i, end=' ')
            print(i, end=' ')
        print()
        return
    # a < 2^M より、K >= 2^M の場合は無理
    if K >= 2**M:
        print(-1)
        return

    B = [i for i in range(0, 2**M) if i != K]
    C = [i for i in range(0, 2**M) if i != K]
    C.reverse()
    # A = B + C とすると、K以外の任意の2つの i について 0 となる（昇順と降順で打ち消しあうため）
    # A = B + [K] + C とすると、K以外の任意の2つの i について K となる
    # A = B + [K] + C + [K] とすると、Kについて sumxor(C) となる
    # あとは sumxor(C) = K となるか否か
    n = 0
    for c in C:
        n ^= c
    if n != K:
        print(-1)
        return
    
    for b in B:
        print(b, end=' ')
    print(K, end=' ')
    for c in C:
        print(c, end=' ')
    print(K)

main()
