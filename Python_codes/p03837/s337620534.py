# https://atcoder.jp/contests/abc051/submissions/1055446

def main():
    import sys
    input = sys.stdin.readline

    inf = 1000 * 100 + 10

    N, M = map(int, input().split())

    dist = [[inf for _ in range(N)] for _ in range(N)]
    for j in range(N):
        dist[j][j] = 0

    es = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        es.append((a, b, c))
        dist[a][b] = dist[b][a] = c

    for k in range(N):
        for j in range(N):
            for i in range(j):
                d = dist[i][k] + dist[k][j]
                if dist[i][j] > d:
                    dist[i][j] = dist[j][i] = d

    ans = 0
    for a, b, c in es:
        if dist[a][b] == c: continue
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
