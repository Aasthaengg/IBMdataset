#!/usr/bin/env python
"""東京海上日動　プログラミングコンテスト2020: A - Tag
https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_b
"""


def run(a, vt, b, wt):
    if a < b:
        if b + wt <= a + vt:
            return 'YES'
        else:
            return 'NO'
    else:
        if a - vt <= b - wt:
            return 'YES'
        else:
            return 'NO'


def main():
    A, V = list(map(int, input().split()))
    B, W = list(map(int, input().split()))
    T = int(input())

    print(run(A, V*T, B, W*T))


if __name__ == '__main__':
    main()
