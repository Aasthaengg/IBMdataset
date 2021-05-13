def resolve():
    def BF(s, n, edge, inf=float("inf")):
        d = [inf for i in range(n)]
        d[s] = 0
        for i in range(n * 2):
            for before, after, dist in edge:
                if before != inf and d[before] + dist < d[after]:
                    if i < n:
                        d[after] = d[before] + dist
                    else:
                        d[after] = -inf
        return d
    n, m, p = map(int, input().split())
    inf = float("inf")
    edge = [list(map(int, input().split())) for _ in range(m)]
    edge = [[x - 1, y - 1, p - z] for x, y, z in edge]
    ans = -BF(0, n, edge, inf)[-1]
    print(max(0, ans) if ans < inf else -1)


if __name__ == "__main__":
    resolve()
