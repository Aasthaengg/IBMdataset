import sys
input = sys.stdin.readline


def read():
    _, _, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    XYC = []
    for i in range(M):
        x, y, c = map(int, input().strip().split())
        XYC.append((x, y, c))
    return A, B, M, XYC


def solve(A, B, M, XYC):
    min_cost = min(A) + min(B)
    for x, y, c in XYC:
        cost = A[x-1] + B[y-1] - c
        min_cost = min(min_cost, cost)
    return min_cost


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
