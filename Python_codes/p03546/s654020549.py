import sys
read = sys.stdin.read
from itertools import chain
from collections import Counter
def main():
    def warshall_floyd(d):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d

    h, w = map(int, input().split())
    n = 10
    d = [[10**9] * 10 for _ in range(10)]
    for i1 in range(10):
        row = tuple(map(int, input().split()))
        for i2 in range(10):
            d[i1][i2] = row[i2]
    res = warshall_floyd(d)
    hw = [list(map(int, input().split())) for _ in range(h)]
    hw1d = chain.from_iterable(hw)
    hw1dc = Counter(hw1d)
    r = 0
    for j1 in range(10):
        r += hw1dc[j1] * res[j1][1]
    print(r)

if __name__ == '__main__':
    main()