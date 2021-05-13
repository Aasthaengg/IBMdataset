import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    X = list(map(int, input().split()))

    for i in range(n):
        if X[i] >= 0:
            ori = i
            X.insert(ori, 0)
            break
    else:
        ori = n
        X.insert(ori, 0)

    res = f_inf
    start = max(0, ori - k)
    end = min(n - k + 1, ori + 1)
    for j in range(start, end):
        left = abs(X[j]) * 2 + abs(X[j + k])
        right = abs(X[j]) + abs(X[j + k]) * 2
        res = min(res, min(left, right))
    print(res)


if __name__ == '__main__':
    resolve()
