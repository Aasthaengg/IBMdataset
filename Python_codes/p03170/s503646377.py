import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from operator import xor
from functools import reduce

N,K,*A = map(int,read().split())

a = reduce(xor,(1<<a for a in A))

dp = 0 # bitset
for n in range(K):
    if not(dp&(1<<n)):
        dp |= (a<<n)

answer = 'First' if dp&(1<<K) else 'Second'
print(answer)