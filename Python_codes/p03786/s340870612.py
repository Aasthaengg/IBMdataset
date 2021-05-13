from bisect import bisect_right
from itertools import accumulate


def can_survive(prev):
    while True:
        idx = bisect_right(A, 2 * acc_A[prev]) - 1
        if idx == N - 1:
            return True
        if idx == prev:
            return False
        prev = idx


def binary_search(left, right):
    while right - left > 1:
        mid = (left + right) // 2
        if can_survive(mid):
            right = mid
        else:
            left = mid
    return left if can_survive(left) else right


N = int(input())
A = sorted(map(int, input().split()))
acc_A = list(accumulate(A))
print(N - binary_search(0, N))
