import sys
input = sys.stdin.readline


def read():
    N, K = map(int, input().strip().split())
    X = list(map(int, input().strip().split()))
    return N, K, X


def solve(N, K, X):
    amin = 10**9
    for i in range(N-K+1):
        a0 = min(abs(X[i+K-1]), abs(X[i]))
        a1 = abs(X[i+K-1] - X[i])
        amin = min(amin, a0 + a1)
    return amin


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
