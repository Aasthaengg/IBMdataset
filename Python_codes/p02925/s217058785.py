import sys
read = sys.stdin.readline


def main():
    n = int(read())
    V = 1000000

    g = [[] for _ in range(V)]
    deg = [0] * V
    vlist = set()

    for i in range(n):
        a = list(map(lambda x: int(x) - 1, read().rstrip().split()))
        for j in range(n - 1):
            v1 = min(i, a[j]) * 1000 + max(i, a[j])
            vlist.add(v1)
            if j == n - 2:
                break
            v2 = min(i, a[j + 1]) * 1000 + max(i, a[j + 1])
            g[v1].append(v2)
            deg[v2] += 1

    d = [0] * V
    check_cnt = 0
    q = []
    for v in vlist:
        if deg[v] == 0:
            q.append(v)

    if len(q) == 0:
        print(-1)
        exit()

    for v in q:
        check_cnt += 1
        for nv in g[v]:
            d[nv] = max(d[nv], d[v] + 1)
            deg[nv] -= 1
            if deg[nv] == 0:
                q.append(nv)
    if check_cnt == n * (n - 1) // 2:
        print(max(d) + 1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
