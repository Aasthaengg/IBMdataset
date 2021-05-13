from collections import deque

def main():
    n = int(input())
    adjacent = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        adjacent[a - 1].append((b - 1, c))
        adjacent[b - 1].append((a - 1, c))
    q, k = map(int, input().split())
    next_search = deque([k - 1])
    searched = set()
    dist = [10**20] * n
    dist[k - 1] = 0
    while next_search:
        p = next_search.popleft()
        if p in searched:
            continue
        searched.add(p)
        for pp, d in adjacent[p]:
            dist[pp] = min(dist[p] + d, dist[pp])
            next_search.append(pp)
    for _ in range(q):
        x, y = map(int, input().split())
        print(dist[x - 1] + dist[y - 1])

if __name__ == '__main__':
    main()