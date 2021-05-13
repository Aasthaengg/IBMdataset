import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = list(map(int, input().split()))
    for i in range(n):
        x = X[i]
        X[i] = [i, x]
    X_s = sorted(X, key=lambda x: x[1])

    res = [0] * n
    for i in range(n):
        idx, _ = X_s[i]
        if i < n // 2:
            res[idx] = X_s[n // 2][1]
        else:
            res[idx] = X_s[n // 2 - 1][1]

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
