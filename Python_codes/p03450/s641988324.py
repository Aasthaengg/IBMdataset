from collections import deque


def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]

    for _ in range(m):
        l, r, d = map(int, input().split())
        adj[l - 1].append((r - 1, d))
        adj[r - 1].append((l - 1, -d))

    x = [None] * n

    for i in range(n):
        if x[i] is not None:
            continue
        x[i] = 0
        q = deque()
        q.append(i)

        while q:
            u = q.popleft()
            for v, d in adj[u]:
                if x[v] is None:
                    q.append(v)
                    x[v] = x[u] + d
                elif x[v] != x[u] + d:
                    print("No")
                    exit()
    print("Yes")


if __name__ == "__main__":
    main()
