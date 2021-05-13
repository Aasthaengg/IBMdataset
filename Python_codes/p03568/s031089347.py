import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    bit = []
    for i in range(n):
        bit.append(list(range(A[i] - 1, A[i] + 2)))

    res = 0
    for pattern in product([0, 1, 2], repeat=n):
        value = 1
        for idx, i in enumerate(pattern):
            value *= bit[idx][i]

        if value % 2 == 0:
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()
