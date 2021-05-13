import collections
import heapq
def main():

    N, M = map(int, input().split())
    graph = collections.defaultdict(dict)
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = -c

    dist = [float('inf') for _ in range(N)]
    dist[0] = 0
    for _ in range(N-1):
        for a in graph:
            for b in graph[a]:
                dist[b] = min(dist[b], dist[a] + graph[a][b])

    ans = dist[N-1]

    negative = [False for _ in range(N)]
    for _ in range(N):
        for a in graph:
            if dist[a] != float('inf'):
                for b in graph[a]:
                    if dist[b] > dist[a] + graph[a][b]:
                        negative[b] = True
                        dist[b] = dist[a] + graph[a][b]
                    if negative[a] == True:
                        negative[b] = True

    if negative[N-1] == True:
        return "inf"
    else:
        return -ans


if __name__ == '__main__':
    print(main())
