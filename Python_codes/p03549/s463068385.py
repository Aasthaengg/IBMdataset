import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
#確率は1/2 ** M
#時間は(N-M) * 100 + M * 1900
answer = ((N-M) * 100 + M * 1900) / 0.5 ** M
print(int(answer))
# 16