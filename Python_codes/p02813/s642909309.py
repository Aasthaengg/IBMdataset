import itertools
import math
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

# 順列のリスト
pmt = list(itertools.permutations(range(1, N + 1), N))

a = 0
b = 0

for i in range(len(pmt)):
    if pmt[i] == P:
        a = i + 1
    if pmt[i] == Q:
        b = i + 1
print(abs(a - b))
