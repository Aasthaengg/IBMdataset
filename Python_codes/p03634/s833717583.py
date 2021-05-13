import sys
readline = sys.stdin.readline
from collections import deque

def main():
    N = int(readline())
    path = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, c = map(int, readline().rstrip().split())
        path[a-1].append((b-1, c))
        path[b-1].append((a-1, c))
    Q, K = map(int, readline().rstrip().split())
    K -= 1

    dist = [-1] * N
    dist[K] = 0
    for n, c in path[K]:
        dist[n] = c
        
    que = deque([(K, n) for n, c in path[K]])
    while que:
        pre, now = que.popleft()
        for next, d in path[now]:
            if next != pre:
                dist[next] = dist[now] + d
                que.append((now, next))

    for _ in range(Q):
        x, y = map(int, readline().rstrip().split())
        print(dist[x-1] + dist[y-1])

if __name__ == '__main__':
    main()