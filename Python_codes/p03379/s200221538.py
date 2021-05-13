# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A = lr()
sorted_A = sorted(A)
mid = N // 2 - 1
left = sorted_A[mid]
right = sorted_A[mid+1]
answer = [left if a > left else right for a in A]
print('\n'.join(map(str, answer)))
