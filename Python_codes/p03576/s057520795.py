from itertools import product
from operator import itemgetter
import sys
def main(N, K, P):
    X = sorted(map(itemgetter(0), P))
    Y = sorted(map(itemgetter(1), P))
    Xd, Yd = dict(), dict()
    for i, (x, y) in enumerate(zip(X, Y)):
        Xd[x] = i
        Yd[y] = i

    C = [[0] * (N + 1) for _ in range(N + 1)]
    for x, y in P:
        i, j = Xd[x] + 1, Yd[y] + 1
        C[i][j] += 1
    for i in range(1, N + 1):
        for j in range(N):
            C[i][j + 1] += C[i][j]
    for j in range(1, N + 1):
        for i in range(N):
            C[i + 1][j] += C[i][j]

    ans = 10**20
    for x1, y1 in product(range(N), repeat=2):
        for x2, y2 in product(range(x1, N), range(y1, N)):
            c = C[x2 + 1][y2 + 1] - C[x1][y2 + 1] - C[x2 + 1][y1] + C[x1][y1]
            if c >= K:
                s = (X[x2] - X[x1]) * (Y[y2] - Y[y1])
                assert s >= 0
                if s != 0:
                    ans = min(ans, s)
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    main(N, K, P)
