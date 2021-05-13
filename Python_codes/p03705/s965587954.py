import sys

N, A, B = map(int, sys.stdin.readline().strip().split())

min_sum = A*(N-1) + B
max_sum = B*(N-1) + A
print(max(0, max_sum - min_sum + 1))