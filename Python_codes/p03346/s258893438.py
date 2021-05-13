import sys
input = sys.stdin.readline
import heapq


def read():
    N = int(input().strip())
    P = []
    for i in range(N):
        p = int(input().strip())
        P.append(p)
    return N, P


def solve(N, P):
    Q = [0 for i in range(N)]
    for i in range(N):
        Q[P[i]-1] = i
    max_count = 0
    count = 0
    prev = -1
    for i in range(N):
        q = Q[i]
        if prev < q:
            count += 1
            prev = q
        else:
            max_count = max(max_count, count)
            count = 1
            prev = q
    max_count = max(max_count, count)
    return N - max_count


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
