import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    T = list(map(int, input().strip().split()))
    M = int(input().strip())
    PX = []
    for i in range(M):
        p, x = map(int, input().strip().split())
        PX.append((p, x))
    return N, T, M, PX


def solve(N, T, M, PX):
    S = sum(T)
    for p, x in PX:
        ans = S - T[p-1] + x
        print(ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
