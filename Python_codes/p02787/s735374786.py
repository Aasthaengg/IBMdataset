import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    H, N = read_ints()
    A, B = [], []
    for _ in range(N):
        a, b = read_ints()
        A.append(a)
        B.append(b)
    OPT = [math.inf for _ in range(H+max(A)+1)]
    OPT[0] = 0
    for h in range(H):
        for i in range(N):
            OPT[h+A[i]] = min(OPT[h+A[i]], OPT[h]+B[i])
    return min(OPT[H:])


if __name__ == '__main__':
    print(solve())
