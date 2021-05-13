import sys
input = sys.stdin.readline
from fractions import gcd


def read():
    N, M = map(int, input().strip().split())
    AB = []
    for i in range(M):
        a, b = map(int, input().strip().split())
        AB.append((a-1, b-1))
    return N, M, AB


def solve(N, M, AB):
    n_neighbors = [0 for i in range(N)]
    for a, b in AB:
        n_neighbors[a] += 1
        n_neighbors[b] += 1
    for x in n_neighbors:
        print(x)


if __name__ == '__main__':
    inputs = read()
    solve(*inputs)
