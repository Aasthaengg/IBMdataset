import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
edges = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b, c = [int(_) for _ in input().split()]
    edges[a].append((b, c))
    edges[b].append((a, c))

L = [-1] * (N + 1)


def w(k):
    que = deque()
    L[k] = 0
    que.append((k, -1))
    while que:
        n, p = que.popleft()
        for nn, nv in edges[n]:
            if nn == p: continue
            L[nn] = L[n] + nv
            que.append((nn, n))


def main():
    q, k = [int(_) for _ in input().split()]
    w(k)
    for i in range(q):
        a, b = [int(_) for _ in input().split()]
        print(L[a] + L[b])

if __name__ == '__main__':
    main()