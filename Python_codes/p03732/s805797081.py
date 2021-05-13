import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, W, *wv = map(int, read().split())

    w0 = wv[0]
    weight = [[] for _ in range(4)]
    for w, v in zip(*[iter(wv)] * 2):
        weight[w - w0].append(v)

    for i in range(4):
        weight[i].sort(reverse=True)

    csum = [[0] for _ in range(4)]
    for i in range(4):
        csum[i].extend(accumulate(weight[i]))

    def dfs(w, v, idx):
        if idx == 4:
            return v

        ans = 0
        for i in range(len(csum[idx])):
            if w + (w0 + idx) * i > W:
                break
            ans = max(ans, dfs(w + (w0 + idx) * i, v + csum[idx][i], idx + 1))

        return ans

    print(dfs(0, 0, 0))

    return


if __name__ == '__main__':
    main()
