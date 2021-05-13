import sys
from collections import defaultdict
import itertools

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N, C = in_nn()
    D = [list(map(int, readline().split())) for _ in range(C)]
    c = [list(map(int, readline().split())) for _ in range(N)]

    grid = [defaultdict(int) for _ in range(3)]

    for y in range(N):
        for x in range(N):
            d = grid[(x + y + 2) % 3]
            d[c[y][x]] += 1

    comb = itertools.permutations(range(1, C + 1), 3)

    ans = 10**9 + 7
    for com in comb:
        iwa = 0
        for i in range(3):
            n_c = com[i]
            for k, v in grid[i].items():
                iwa += D[k - 1][n_c - 1] * v
        ans = min(ans, iwa)

    print(ans)


if __name__ == '__main__':
    main()
