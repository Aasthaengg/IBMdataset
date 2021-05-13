import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    C = []
    for i in range(H):
        c = input()
        C.append(c)
        C.append(c)

    for c in C:
        print(c)


if __name__ == '__main__':
    resolve()
