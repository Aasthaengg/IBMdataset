import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    nums = list(input())
    for pattern in product(["+", "-"],repeat=3):
        pattern = list(pattern) + [""]
        fomula = ""
        for op, num in zip(pattern, nums):
            fomula += num + op
        if eval(fomula) == 7:
            print(fomula + "=" + "7")
            break


if __name__ == '__main__':
    resolve()
