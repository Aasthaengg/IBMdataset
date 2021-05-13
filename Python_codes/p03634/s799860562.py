mod = 1000000007
eps = 10**-9


def main():
    import sys
    from collections import deque
    input = sys.stdin.buffer.readline

    N = int(input())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        adj[b].append((a, c))
    Q, root = map(int, input().split())

    que = deque()
    que.append(root)
    seen = [-1] * (N+1)
    seen[root] = 0
    par = [0] * (N+1)
    child = [[] for _ in range(N+1)]
    seq = []
    while que:
        v = que.popleft()
        seq.append(v)
        for u, c in adj[v]:
            if seen[u] == -1:
                seen[u] = seen[v] + c
                par[u] = v
                child[v].append(u)
                que.append(u)
    seq.reverse()

    for _ in range(Q):
        x, y = map(int, input().split())
        print(seen[x] + seen[y])


if __name__ == '__main__':
    main()
