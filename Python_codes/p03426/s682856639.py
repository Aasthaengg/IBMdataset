import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    H, W, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    M = defaultdict(list)
    for h in range(H):
        for w in range(W):
            M[A[h][w]] = [h, w]
    P = defaultdict(list)
    for d in range(1, D + 1):
        a = d
        while a <= H * W - D:
            p = abs(M[a][0] - M[a + D][0]) + abs(M[a][1] - M[a + D][1])
            if P[d]:
                P[d].append(P[d][-1] + p)
            else:
                P[d] = [0, p]
            a += D
    # print(P)
    Q = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        d = L % D
        l = L // D
        r = R // D
        if d == 0:
            d = D
            if len(P[d]) > 0:
                print(P[d][r - 1] - P[d][l - 1])
            else:
                print(0)
        else:
            if len(P[d])>0:
                print(P[d][r] - P[d][l])
            else:
                print(0)


if __name__ == "__main__":
    main()
