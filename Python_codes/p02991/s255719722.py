def main():
    import sys
    from collections import deque
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    adj = [[] for _ in range(N*3+5)]
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v+N+1)
        adj[u+N+1].append(v+2*N+2)
        adj[u+2*N+2].append(v)

    s, t = map(int, input().split())
    que = deque()
    que.append(s)
    seen = [-1] * (N*3+5)
    seen[s] = 0
    while que:
        v = que.popleft()
        for u in adj[v]:
            if seen[u] == -1:
                seen[u] = seen[v] + 1
                que.append(u)

    if seen[t] == -1:
        print(-1)
    else:
        assert seen[t] % 3 == 0
        print(seen[t] // 3)


if __name__ == '__main__':
    main()
