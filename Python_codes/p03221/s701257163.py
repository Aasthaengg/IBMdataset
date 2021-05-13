import sys
input = sys.stdin.readline


def read():
    N, M = map(int, input().strip().split())
    IPY = []
    for i in range(M):
        p, y = map(int, input().strip().split())
        IPY.append((i, p, y))
    return N, M, IPY


def solve(N, M, IPY):
    X = [1 for i in range(N+1)]
    IPY.sort(key=lambda ipy: ipy[2])
    zipcode = []
    for i, p, y in IPY:
        zipcode.append((i, p, X[p]))
        X[p] += 1
    zipcode.sort()
    for i, p, x in zipcode:
        print("{:06d}{:06d}".format(p, x))


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
