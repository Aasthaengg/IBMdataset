import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import itertools


def main():
    input = sys.stdin.buffer.readline
    h, w = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    a = [list(map(int, input().split())) for _ in range(h)]
    d = floyd_warshall(csgraph=csr_matrix(c, dtype="i8"), directed=True)
    ans = 0
    for n in itertools.chain.from_iterable(a):
        if n != -1:
            ans += int(d[n][1])
    print(ans)


if __name__ == "__main__":
    main()
