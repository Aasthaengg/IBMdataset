# C - Step

from itertools import accumulate
import operator

n = int(input())
a = list(map(int, input().split()))
assert n == len(a)

b = accumulate(a, max)
s = sum(map(operator.sub, b, a))
print(s)
