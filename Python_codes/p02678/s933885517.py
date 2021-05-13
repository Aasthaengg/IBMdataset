from collections import deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N, M = [int(i) for i in input().strip().split()]
    graph = [[] for _ in range(N)]
    sign = [0] * N
    for _ in range(M):
        a, b = [int(i) for i in input().strip().split()]
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    candidates = deque([0])
    visited = [False] * N
    visited[0] = True
    while len(candidates) > 0:
        v = candidates.popleft()
        for i in graph[v]:
            if visited[i]:
                continue
            visited[i] = True
            sign[i] = v
            candidates.append(i)
    print("Yes")
    for i in sign[1:]:
        print(i + 1)

    return


if __name__ == "__main__":
    main()
