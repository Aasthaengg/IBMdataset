import sys
input = sys.stdin.readline


def read():
    N = int(input().strip())
    return N,


def solve(N):
    L = [0 for i in range(N+1)]
    L[0] = 2
    L[1] = 1
    for i in range(2, N+1):
        L[i] = L[i-1] + L[i-2]
    return L[N]


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
