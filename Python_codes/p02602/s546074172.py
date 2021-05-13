#!/usr/bin/env python
"""M-SOLUTIONS プロコンオープン 2020: C - Marks
https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_c
"""


def main():
    N, K = list(map(int, input().split()))
    As = list(map(int, input().split()))

    for i in range(0, N-K):
        prev_score = As[i]
        score = As[K + i]
        if prev_score < score:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
