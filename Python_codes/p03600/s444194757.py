def main():
    N = int(input())
    A = []
    dist = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        Ai = list(map(int, input().split()))
        A.append(Ai)
        for j in range(N):
            dist[i][j] = Ai[j]

    def wf(dist):
        need = [[1 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        print(-1)
                        exit()
                    elif dist[i][j] == dist[i][k] + dist[k][j]:
                        if i != k and j != k:
                            need[i][j] = 0
                            need[j][i] = 0
        return need

    need = wf(dist)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += need[i][j] * dist[i][j]
    print(ans)


if __name__ == '__main__':
    main()
