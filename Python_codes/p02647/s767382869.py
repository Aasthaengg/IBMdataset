import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(k if k < 60 else 60):
        imos = [0] * (n + 1)
        for i in range(n):
            left = max(0, i - A[i])
            imos[left] += 1
            right = min(n, i + A[i] + 1)
            imos[right] -= 1

        B = list(accumulate(imos))
        A = B
    print(*A[:n])


if __name__ == '__main__':
    resolve()
