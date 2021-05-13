from heapq import heappush, heappop, heapreplace

def main():
    INF = 10 ** 9 + 7

    N, K, *TD = map(int, open(0).read().split())

    E = [[] for _ in range(N)]
    for t, d in zip(*[iter(TD)] * 2):
        E[t - 1].append(d)

    for e in E:
        if e:
            e.sort(reverse=True)
        else:
            e.append(-INF)
    E.sort(key=lambda x: -x[0])

    cur = 0
    Q = []
    for i in range(K):
        cur += E[i][0]
        for j in range(1, len(E[i])):
            heappush(Q, -E[i][j])

    for i in range(K, N):
        for eij in E[i]:
            heappush(Q, -eij)

    res = cur + K * K
    for x in reversed(range(1, K)):
        v, w = E[x][0], -Q[0]
        if v < w:
            heapreplace(Q, -v)
            cur += w - v

        tmp = cur + x * x
        if res < tmp:
            res = tmp

    print(res)

if __name__ == '__main__':
    main()
