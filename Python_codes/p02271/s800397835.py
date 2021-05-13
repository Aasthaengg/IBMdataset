import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    M = list(map(int, input().split()))

    num = set()
    for pattern in product([0, 1], repeat=n):
        total = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                total += A[idx]
        num.add(total)

    for m in M:
        print("yes" if m in num else "no")


if __name__ == '__main__':
    resolve()

