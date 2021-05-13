import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    C = list(map(int, input().split()))
    C.sort(reverse=True)

    s = sum(C[1:])
    ans = [None] * N

    # c, node
    q = deque([(0, 0)])
    ans[0] = C[0]
    visited = [False] * N
    visited[0] = True
    used = [False] * N
    used[0] = True

    while q:
        c, node = q.popleft()

        for j in edges[node]:
            if visited[j]:
                continue

            for k in range(c + 1, N):
                if used[k]:
                    continue
                else:
                    next_c = k
                    break

            visited[j] = True
            used[next_c] = True
            ans[j] = C[next_c]
            q.append((next_c, j))

    print(s)
    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
