#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    kmax = ((n - 1) * (n - 2)) // 2
    if k > kmax:
        print(-1)
        return

    edges = getedges(n, k, kmax)
    print(len(edges))
    for i, j in edges:
        print(i, j)

def getedges(n, k, kmax):
    edges = []
    for i in range(1, n):
        edges.append((i, n))
    if kmax == k:
        return edges
    c = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            edges.append((i, j))
            c += 1
            if c == kmax - k:
                return edges
    assert False

if __name__ == "__main__":
    main()
