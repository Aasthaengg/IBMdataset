import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y, z, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB = sorted(AB, reverse=True)[:k]

    res = []
    for ab in AB:
        for c in C:
            res.append(ab + c)
    res = sorted(res, reverse=True)[:k]
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
