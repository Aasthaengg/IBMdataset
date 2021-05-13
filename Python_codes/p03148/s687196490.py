from heapq import heappush, heapreplace

def main():
    INF = 10 ** 9 + 5

    N, K, *TD = map(int, open(0).read().split())

    E = [[-INF] for _ in range(N)]
    for t, d in zip(*[iter(TD)] * 2):
        E[t - 1].append(d)

    for e in E:
        e.sort(reverse=True)
    E.sort(key=lambda x: -x[0])

    cur = 0
    Q = []
    for ei in E[:K]:
        cur += ei[0]
        for eij in ei[1:]:
            heappush(Q, -eij)

    for ei in E[K:]:
        for eij in ei:
            heappush(Q, -eij)

    res = cur + K * K
    for x in reversed(range(1, K)):
        v, w = E[x][0], -Q[0]
        if v < w:
            heapreplace(Q, -v)
            cur += w - v

        res = max(res, cur + x * x)

    print(res)

if __name__ == '__main__':
    main()
