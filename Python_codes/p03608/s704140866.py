import sys
import heapq
import itertools

INF = 10**18

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def dijkstra(N, s0, edge):

    d = [INF] * N
    pre_v = [-1] * N
    used = [False] * N
    edgelist = [(0, s0, -1)]
    heapq.heapify(edgelist)

    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue

        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        pre_v[v] = minedge[2]

        for e in edge[v]:
            if d[e[1]] <= (e[0] + d[v]) or used[e[1]]:
                continue
            heapq.heappush(edgelist, (e[0] + d[v], e[1], v))
    return d, pre_v


def main():

    N, M, R = in_nn()
    r = in_nl()
    r = [t - 1 for t in r]
    edge = [[] for _ in range(N)]

    for i in range(M):
        a, b, c = in_nn()
        a, b = a - 1, b - 1
        edge[a].append((c, b))
        edge[b].append((c, a))

    dis = [[-1] * N for _ in range(N)]
    for i in range(R):
        s = r[i]
        d, pre_v = dijkstra(N, s, edge)

        for j in range(R):
            e = r[j]
            dis[s][e] = d[e]

        for j in range(R):
            if i == j:
                continue

            e = r[j]
            tr = set(r) - {e} - {s}
            while e != -1:
                t = pre_v[e]
                if t in tr:
                    dis[s][e] = -1
                    break
                else:
                    e = t

    perm = itertools.permutations(r, R)

    ans = INF
    for per in perm:

        td = 0
        for i in range(R - 1):
            s, e = per[i], per[i + 1]
            if dis[s][e] == -1:
                break
            else:
                td += dis[s][e]
        else:
            ans = min(ans, td)

    # print(dis)
    print(ans)


if __name__ == '__main__':
    main()
