import unittest

import collections


def solve(n, tree):
    cl = [0] * n
    visited = [False]*n
    stack = []
    stack.append((0, 0))
    while stack:
        v, c = stack.pop()
        if visited[v]:
            continue
        cl[v] = c
        visited[v] = True
        for nv, w in tree[v]:
            if visited[nv]:
                continue
            stack.append((nv, (c + w) % 2))

    return '\n'.join([str(c) for c in cl])


def main():
    n = int(input())
    tree = [[] for i in range(n)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        tree[v-1].append((u-1, w % 2))
        tree[u-1].append((v-1, w % 2))
    result = solve(n, tree)
    print(result)


if __name__ == "__main__":
    main()
