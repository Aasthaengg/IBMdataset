import sys
input = sys.stdin.readline
from itertools import product


def read():
    N, K = map(int, input().strip().split())
    return N, K


def binom2(n):
    return n * (n-1) // 2


def print_graph(pairs):
    print(len(pairs))
    for x, y in pairs:
        print("%d %d" % (x, y))


def solve(N, K):
    B = binom2(N-1)
    if K > B:
        print(-1)
        return
    XY = []
    y = N
    for x in range(1, N):
        XY.append((x, y))
    k = B
    # k=0でB対あるので、K対になるまで辺を1本ずつ増やす
    for x in range(1, N):
        for y in range(x+1, N):
            if k == K:
                print_graph(XY)
                return
            XY.append((x, y))
            k -= 1
    print_graph(XY)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
