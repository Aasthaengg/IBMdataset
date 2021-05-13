import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A, B, C, K = lr()
if K%2 == 0:
    answer = A - B
else:
    answer = B - A

if answer > 10 ** 18:
    answer = 'Unfair'

print(answer)
