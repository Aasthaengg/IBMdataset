import sys
import numpy as np
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = np.array(list(map(int, input().split())), dtype='i8')
    ans = np.zeros(N, dtype='i8')
    A = A * 2
    s = np.sum(A) // 2

    na1 = 0
    for i in range(1, N, 2):
        na1 += A[i]

    ans[0] = s - na1
    for i in range(N - 1):
        ans[i + 1] = A[i] - ans[i]

    print(' '.join(map(str, ans.tolist())))


if __name__ == '__main__':
    solve()
