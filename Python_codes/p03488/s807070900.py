import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    X, Y = map(int, input().split())

    S = list(map(len, S.split("T")))
    init_x = S[0]
    is_x = 0
    to_x, to_y = [], []
    for i in range(1, len(S)):
        if S[i]:
            to_x.append(S[i]) if is_x else to_y.append(S[i])
        is_x ^= 1

    now_x = {init_x}
    for x in to_x:
        tmp = set()
        for now in now_x:
            tmp.add(now - x)
            tmp.add(now + x)
        now_x = tmp

    now_y = {0}
    for y in to_y:
        tmp = set()
        for now in now_y:
            tmp.add(now - y)
            tmp.add(now + y)
        now_y = tmp

    print("Yes" if X in now_x and Y in now_y else "No")


if __name__ == '__main__':
    resolve()
