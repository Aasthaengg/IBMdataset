import sys
from collections import deque

input = sys.stdin.readline


def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    C = list(map(int, input().split()))
    C.sort(reverse=True)

    M = sum(C[1:])
    d = [0] * N
    i = 0
    queue = deque([(i, -1)])
    while queue:
        u, p = queue.popleft()
        d[u] = C[i]
        i += 1
        for v in G[u]:
            if v == p: continue
            queue.append((v, u))

    print(M)
    print(" ".join(map(str, d)))


if __name__ == "__main__":
    main()
