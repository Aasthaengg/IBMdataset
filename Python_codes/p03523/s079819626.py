import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    AKIBA = []
    for pattern in product([0, 1], repeat=4):
        L = list("AKIHABARA")
        for idx, p in enumerate(pattern):
            if p == 1:
                if idx == 0:
                    L[0] = ""
                elif idx == 1:
                    L[4] = ""
                elif idx == 2:
                    L[6] = ""
                else:
                    L[8] = ""
        AKIBA.append("".join(L))

    print("YES" if s in AKIBA else "NO")


if __name__ == '__main__':
    resolve()
