import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()
    White = [0] * (n + 1)
    Black = [0] * (n + 1)

    for i in range(n):
        if S[i] == "#":
            Black[i + 1] = Black[i] + 1
        else:
            Black[i + 1] = Black[i]

    for i in reversed(range(n)):
        if S[i] == ".":
            White[i] = White[i + 1] + 1
        else:
            White[i] = White[i + 1]

    res = f_inf
    for i in range(n + 1):
        res = min(res, White[i] + Black[i])

    print(res)


if __name__ == '__main__':
    resolve()
