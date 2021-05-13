import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from fractions import gcd
from functools import reduce

N,K,*A = map(int,read().split())
g = reduce(gcd,A)
x = max(A)

bl = (K<=x) and (K%g==0)
ans = 'POSSIBLE' if bl else 'IMPOSSIBLE'
print(ans)