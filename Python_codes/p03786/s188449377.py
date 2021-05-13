import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')


def resolve():
    n = int(input())
    A = sorted(list(map(int, input().split())))

    R = [0] + list(accumulate(A))
    left = 0
    for i in range(n):
        if R[i] * 2 < A[i]:
            left = i
    print(n - left)


if __name__ == '__main__':
    resolve()
