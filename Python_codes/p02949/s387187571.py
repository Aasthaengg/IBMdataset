import sys
import queue
input = sys.stdin.readline

def main():
    N, M, P = map(int, input().split())
    g = [[] for _ in range(N+1)]
    g2 = [[] for _ in range(N+1)]
    data = [list(map(int, input().split())) for _ in range(M)]
    for a, b, _ in data:
        g2[b].append(a)
        g[a].append(b)

    visit = [False]*(N+1)
    visit2 = [False]*(N+1)

    q = queue.Queue()
    q.put(1)
    visit[1] = True
    while (not q.empty()):
        now = q.get()
        for next in g[now]:
            if not visit[next]:
                visit[next] = True
                q.put(next)

    q = queue.Queue()
    q.put(N)
    visit2[N] = True
    while (not q.empty()):
        now = q.get()
        for next in g2[now]:
            if not visit2[next]:
                visit2[next] = True
                q.put(next)

    for i in range(1, N+1):
        visit[i] = visit[i] and visit2[i]


    INF = 1000000001
    d = [(-1)*INF for i in range(N+1)]
    d[1] = 0

    for i in range(N):
        d_N = [d[i] for i in range(1, N+1) if visit[i]]
        for j in range(M):
            a = data[j][0]
            b = data[j][1]
            c = data[j][2]
            d[b] = max(d[b], d[a]+c-P)
        if i == N-1:
            if d_N != [d[i] for i in range(1, N+1) if visit[i]]:
                ans = -1

            else:
                ans = d[N]

    if ans == -1:
        print(-1)
    else:
        print(max(0, ans))

if __name__ == "__main__":
    main()
