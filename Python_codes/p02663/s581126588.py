#!/usr/bin/env python
"""NOMURA プログラミングコンテスト 2020: A - Study Scheduling
https://atcoder.jp/contests/nomura2020/tasks/nomura2020_a
"""


def main():
    H1, M1, H2, M2, K = list(map(int, input().split()))

    minuts = (H2 - H1) * 60 + (M2 - M1)
    print(minuts - K)


if __name__ == '__main__':
    main()
