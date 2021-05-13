import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    b = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == "#":
            cnt += 1
        b[i] = cnt

    w = [0] * n
    cnt = 0
    for i in reversed(range(n)):
        if s[i] == ".":
            cnt += 1
        w[i] = cnt

    res = f_inf
    w = w + [0]
    b = [0] + b
    for i, j in zip(w, b):
        res = min(res, i + j)
    print(res)


if __name__ == '__main__':
    resolve()
