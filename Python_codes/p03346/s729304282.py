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
    h = []
    for i in range(N):
        heapq.heappush(h, (P[i], i+1))
    max_count = 0
    count = 0
    prev = -1
    for _ in range(N):
        p, i = heapq.heappop(h)
        if prev < i:
            count += 1
            prev = i
        else:
            max_count = max(max_count, count)
            count = 1
            prev = i
    max_count = max(max_count, count)
    return N - max_count


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
