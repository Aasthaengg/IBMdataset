import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input().split("T"))
    gx, gy = map(int, input().split())

    to_X = 0
    init_x = len(S[0])
    S.pop(0)
    X, Y = [], []
    for s in S:
        X.append(len(s)) if to_X else Y.append(len(s))
        to_X ^= 1

    now_x = {init_x}
    for x in X:
        tmp = set()
        for prev_x in now_x:
            tmp.add(prev_x + x)
            tmp.add(prev_x - x)
        now_x = tmp

    now_y = {0}
    for y in Y:
        tmp = set()
        for prev_y in now_y:
            tmp.add(prev_y + y)
            tmp.add(prev_y - y)
        now_y = tmp

    print("Yes" if gx in now_x and gy in now_y else "No")


if __name__ == '__main__':
    resolve()
