import operator
import functools
N = int(input())
S = input()
c = [1] * 26
for s in S:
    c[ord(s)-ord('a')] += 1
print((functools.reduce(operator.mul,c)-1) % (10**9+7))

