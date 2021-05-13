import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

K, X = lr()
bl = 500 * K >= X
print('Yes' if bl else 'No')
# 35