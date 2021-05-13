from collections import deque


def main():

    N, M = map(int, input().split())
    E = [list(map(int, input().split())) for _ in range(M)]

    # make graph
    G = [set() for _ in range(N)]
    for i in range(M):
        E[i][0], E[i][1] = E[i][0] - 1, E[i][1] - 1
        G[E[i][0]].add(E[i][1])

    def bfs(s):
        # find connected vertex by bfs
        vis_loc = [False] * N
        vis_loc[s] = True
        q = deque([s])
        while len(q):
            v = q.popleft()
            for n in G[v]:
                if vis_loc[n]:
                    continue
                q.append(n)
                vis_loc[n] = True
        return vis_loc
    vis = bfs(0)
    C = []
    for i in range(M):
        if vis[E[i][0]]:
            C.append(i)

    # Bellman-Ford
    N_con = sum(vis)
    ans = [float('inf')] * N
    ans[0] = 0
    for i in range(N_con):
        ud = -1
        for j in C:
            a, b, c = E[j]
            if ans[b] > ans[a] - c:
                ans[b] = ans[a] - c
                ud = a
        if ud == -1:
            break
        else:
            if i == N_con - 1:
                if bfs(ud)[N - 1]:
                    print('inf')
                    exit()
    print(-ans[N - 1])


if __name__ == '__main__':
    main()
