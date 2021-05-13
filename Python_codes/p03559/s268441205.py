import bisect
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = sorted(A)
B = sorted(B)
C = sorted(C)


def my_func(A, B, C):
    acc_a = [0]*N
    acc_c = [0]*N

    i_a = 0
    i_c = N-1
    for i in range(N):
        b = B[i]
        while i_a < N and A[i_a] < b:
            acc_a[i] += 1
            i_a += 1

    for i in reversed(range(N)):
        b = B[i]
        while i_c >= 0 and C[i_c] > b:
            acc_c[i] += 1
            i_c -= 1

    acc_a = list(accumulate(acc_a))
    acc_c = list(accumulate(acc_c[::-1]))
    acc_c = acc_c[::-1]

    ans = 0
    for a, c in zip(acc_a, acc_c):
        ans += a*c


def bisect_func(A, B, C):
    acc_a = [0]*N
    acc_c = [0]*N
    for i in range(N):
        acc_a[i] = bisect.bisect_left(A, B[i])
        acc_c[i] = N-bisect.bisect_right(C, B[i])

    ans = 0
    for a, c in zip(acc_a, acc_c):
        ans += a*c
    return ans


print(bisect_func(A, B, C))
