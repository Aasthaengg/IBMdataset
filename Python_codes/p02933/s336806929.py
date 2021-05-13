import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

A = ir()
S = sr()
print(S if A >= 3200 else 'red')
