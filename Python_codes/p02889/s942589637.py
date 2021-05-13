import sys

input = sys.stdin.readline


class AtCoder:
    def main(self):
        N, M, L = map(int, input().split())
        ABC = [tuple(map(int, input().split())) for _ in range(M)]
        Q = int(input())
        st = [tuple(map(int, input().split())) for _ in range(Q)]

        INF = 10 **10
        load = [[INF] * N for _ in range(N)]
        for a, b, c in ABC:
            a -= 1
            b -= 1
            load[a][b] = c
            load[b][a] = c

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    load[i][j] = min(load[i][j], load[i][k] + load[k][j])

        load2 = [[INF] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if load[i][j] <= L:
                    load2[i][j] = 1

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    load2[i][j] = min(load2[i][j], load2[i][k] + load2[k][j])

        for s, t in st:
            s -=1
            t-=1
            if load2[s][t] == INF:
                print(-1)
            else:
                print(load2[s][t] - 1)


# Run main
if __name__ == '__main__':
    AtCoder().main()
