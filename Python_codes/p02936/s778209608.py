from collections import deque


def main():
    n, m = map(int, input().split())

    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        adj[a].append(b)
        adj[b].append(a)

    ans = [0 for _ in range(n)]
    for _ in range(m):
        p, x = map(int, input().split())
        p -= 1
        ans[p] += x

    q = deque()
    q.append(0)
    visited = [False] * n
    visited[0] = True

    while q:
        u = q.pop()
        for v in adj[u]:
            if visited[v]:
                continue
            ans[v] += ans[u]
            q.append(v)
            visited[v] = True

    print(*ans)


if __name__ == "__main__":
    main()
