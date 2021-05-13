import sys
import itertools

input = sys.stdin.readline


def main():
    H, W, D = [int(x) for x in input().split()]
    A = [[int(x) for x in input().split()] for _ in range(H)]
    Q = int(input())
    LR = [[int(x) for x in input().split()] for _ in range(Q)]

    d = {}
    for j in range(H):
        for i in range(W):
            d[A[j][i]] = (i, j)

    A = [[0] for j in range(D)]

    for i in range(D):
        accumu = 0
        for j in range(i, H * W + 1, D):
            if j <= D:
                continue
            accumu += abs(d[j][0] - d[j - D][0]) + abs(d[j][1] - d[j - D][1])
            A[i].append(accumu)


    for l, r in LR:
        if l % D == 0:
            print(A[l % D][r // D - 1] - A[l % D][l // D - 1])
        else:
            print(A[l % D][r // D] - A[l % D][l // D])


if __name__ == '__main__':
    main()
