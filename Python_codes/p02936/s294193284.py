
# copy from https://atcoder.jp/contests/abc138/submissions/15674047

import sys
import heapq
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, Q = map(int, input().split())
    tree = [[] for _ in range(N)]

    for _ in range(N - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        tree[a].append(b)
        tree[b].append(a)

    counter = [0] * N

    for _ in range(Q):
        p, x = map(int, input().split())
        counter[p - 1] += x

    visited = set()
    stack = [0]
    while stack:  # 深さ優先
        i = stack.pop()
        visited.add(i)
        for j in tree[i]:
            if not j in visited:  # 逆方向回るの防止
                counter[j] += counter[i]
                stack.append(j)
    print(*counter)


if __name__ == "__main__":
    main()
