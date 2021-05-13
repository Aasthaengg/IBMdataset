import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
from collections import deque
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, Q = map(int, readline().split())
    AB = list(list(map(int, readline().split())) for _ in range(N-1))
    PX = list(list(map(int, readline().split())) for _ in range(Q))

    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    value = [0] * N
    for p, x in PX:
        value[p-1] += x

    que = deque([0])
    visited = [False]*N
    while que:
        x = que.popleft()
        visited[x] = True
        for y in graph[x]:
            if visited[y]:
                continue
            else:
                value[y] += value[x]
                que.append(y)
    print(' '.join(map(str, value)))


if __name__ == '__main__':
    main()

