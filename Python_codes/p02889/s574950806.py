def main():
    INF = 10 ** 12
    N, M, L = list(map(int, input().split(' ')))
    D = [[INF for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        A, B, C = list(map(int, input().split(' ')))
        A -= 1
        B -= 1
        D[A][B] = C
        D[B][A] = C
    Q = int(input())
    query_list = [list(map(lambda x: int(x) - 1, input().split(' '))) for _ in range(Q)]
    # calc min cost by warshall-floyd method
    for via in range(N):
        for s in range(N):
            for t in range(N):
                d = D[s][via] + D[via][t]
                if D[s][t] > d:
                    D[s][t] = d
                    D[t][s] = d
    # calc min number of charges
    counts = [[INF for _ in range(N)] for _ in range(N)]
    for s in range(N):
        for t in range(N):
            if D[s][t] <= L:
                counts[s][t] = 1
                counts[t][s] = 1
    for via in range(N):
        for s in range(N):
            for t in range(N):
                d = counts[s][via] + counts[via][t]
                if counts[s][t] > d:
                    counts[s][t] = d
                    counts[t][s] = d
    # answer query
    for query in query_list:
        s, t = query
        if counts[s][t] >= INF:
            print(-1)
        else:
            print(counts[s][t] - 1)


if __name__ == '__main__':
    main()