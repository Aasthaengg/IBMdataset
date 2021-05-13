from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from sys import stdin


def makeConnected(n, connections):
    l = list(zip(*connections))
    d = [1] * len(connections)
    a = csr_matrix((d, (l[0], l[1])), (n, n))
    return connected_components(a, return_labels=0)


def main():
    input = lambda: stdin.readline()[:-1]
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in [0] * M]

    ab = [[a - 1, b - 1] for a, b in AB]
    ans = makeConnected(N, ab) - 1
    print(ans)


main()
