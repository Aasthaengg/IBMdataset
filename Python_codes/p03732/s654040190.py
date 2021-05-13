# Editorial

import sys
from itertools import accumulate

def main():
    input = sys.stdin.readline
    N, W = map(int, input().split())

    V = [[] for _ in range(4)]
    w0, v0 = map(int, input().split())
    V[0].append(v0)
    for _ in range(N-1):
        w, v = map(int, input().split())
        V[w-w0].append(v)

    for i in range(4):
        V[i] = list(accumulate([0] + sorted(V[i], key=lambda x: -x)))

    ans = 0
    for i in range(len(V[0])):
        for j in range(len(V[1])):
            for k in range(len(V[2])):
                weight = w0 * i + (w0 + 1) * j + (w0 + 2) * k
                if weight <= W:
                    l  = min(len(V[3]) - 1, (W - weight) // (w0 + 3))
                    ans = max(ans, V[0][i] + V[1][j] + V[2][k] + V[3][l])

    return ans


if __name__ == '__main__':
    print(main())
