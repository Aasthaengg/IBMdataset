def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    def dfs(s) -> list:
        init = n

        d = [init] * n
        d[s] = 0

        q = deque()
        q.append(s)
        while q:
            v = q.popleft()
            for u in g[v]:
                if d[u] != init:
                    continue
                d[u] = d[v] + 1
                q.append(u)

        return d

    n = int(input())

    g = tuple(set() for _ in range(n))
    for _ in range(n - 1):
        a, b = (int(x) - 1 for x in input().split())
        g[a].add(b)
        g[b].add(a)

    dist_1 = dfs(0)
    dist_n = dfs(n - 1)

    fennec = sum(dist_1[v] <= dist_n[v] for v in range(n))
    snuke = n - fennec

    if fennec > snuke:
        print('Fennec')
    else:
        print('Snuke')


if __name__ == '__main__':
    main()
