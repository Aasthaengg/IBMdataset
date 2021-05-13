import sys
import collections


def solve():
    sys.setrecursionlimit(2000)
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    h, w, n = list(map(int, input().rstrip('\n').split()))
    d = collections.defaultdict(int)
    for _ in range(n):
        a, b = list(map(int, input().rstrip('\n').split()))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 1 <= a-1+i < h-1 and 1 <= b-1+j < w-1:
                    d[a-1+i, b-1+j] += 1
    nd = []
    for k, v in d.items():
        nd.append(v)
    nd = collections.Counter(nd)
    print((h - 2) * (w - 2) - sum(nd.values()))
    for i in range(1, 10):
        print(nd[i])


if __name__ == '__main__':
    solve()
