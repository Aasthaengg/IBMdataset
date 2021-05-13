# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
from collections import deque
import sys
def main(N, M, G, S, T):
    INF = 10**10
    q = deque([S])
    dist = [INF] * (3 * N)
    dist[S] = 0
    while q:
        v = q.popleft()
        for to in G[v]:
            if dist[to] < INF: continue
            dist[to] = dist[v] + 1
            q.append(to)
    print(dist[T] // 3 if dist[T] < INF else -1)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N * 3)]
    for _ in range(M):
        x, y = map(int, input().split())
        x, y = x - 1, y - 1
        G[x].append(y + N)
        G[x + N].append(y + N + N)
        G[x + N + N].append(y)
    S, T = map(lambda x: int(x) - 1, input().split())
    main(N, M, G, S, T)
