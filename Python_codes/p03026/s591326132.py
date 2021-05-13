def main():
    import sys
    sys.setrecursionlimit(10 ** 7)

    def dfs(v):
        nonlocal curr

        num[v] = 0  # 0: visited, but not written yet

        for u in g[v]:
            if num[u] >= 0:
                continue
            dfs(u)
        num[v] = c[curr]
        curr += 1

    n = int(input())

    g = [set() for _ in range(n)]
    for _ in range(n - 1):
        a, b = (int(x) - 1 for x in input().split())
        g[a].add(b)
        g[b].add(a)
        # 出次数は、len(g[x])-1
        # 親を除いた残りが子
    *c, = sorted(map(int, input().split()))

    num = [-1] * n
    curr = 0
    dfs(0)

    print(sum(c[:-1]))
    print(*num)


if __name__ == '__main__':
    main()
