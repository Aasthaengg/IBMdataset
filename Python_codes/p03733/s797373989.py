import sys
input = sys.stdin.readline


def read():
    N, T = map(int, input().strip().split())
    U = map(int, input().strip().split())
    return N, T, U


def solve(N, T, U):
    tsum = 0
    t0 = 0
    for t1 in sorted(list(U)):
        if t1 - t0 < T:
            tsum += t1 - t0
        else:
            tsum += T
        t0 = t1
    return tsum + T


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
