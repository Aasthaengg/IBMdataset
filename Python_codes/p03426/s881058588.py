import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    H, W, D = map(int, input().split())
    A = []
    for _ in range(H):
        a = list(map(int, input().split()))
        A.append(a)

    place = {}
    for h in range(H):
        for w in range(W):
            place[A[h][w]] = (h, w)

    diff = dict()
    for d in range(1, D + 1):
        cumsum = [0]
        ds = list(range(d, H * W + 1, D))
        N = len(ds)
        for i in range(N - 1):
            x, y = place[ds[i]]
            X, Y = place[ds[i + 1]]
            tmp = cumsum[-1] + abs(x - X) + abs(y - Y)
            cumsum.append(tmp)
        diff[d % D] = cumsum

    Q = int(input())
    ans = []
    for _ in range(Q):
        L, R = map(int, input().split())
        m = L % D
        if m == 0:
            L_idx = L // D - 1
            R_idx = R // D - 1
        else:
            L_idx = L // D
            R_idx = R // D
        a = diff[m][R_idx] - diff[m][L_idx]
        ans.append(a)

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
