import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, D = lr()
# 2 * D + 1
answer = (N + 2 * D) // (2 * D + 1)
print(answer)
