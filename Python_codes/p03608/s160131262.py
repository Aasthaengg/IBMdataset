from itertools import permutations


def main():
    N, M, R = map(int, input().split())
    r = list(map(lambda x: int(x) - 1, input().split()))
    dist = [[1001001001 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        dist[a][b] = c
        dist[b][a] = c
    for i in range(N):
        dist[i][i] = 0

    # warshall-floyd
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    ans = 1001001001
    for way in permutations(r):
        ans_now = 0
        for i in range(R - 1):
            ans_now += dist[way[i]][way[i + 1]]
        if ans > ans_now: ans = ans_now
    print(ans)


if __name__ == '__main__':
    main()
