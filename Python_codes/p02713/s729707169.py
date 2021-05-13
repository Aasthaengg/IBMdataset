import math
from functools import reduce
import sys
sys.setrecursionlimit(2000000)

k = int(input())

wa = 0

for a in range(1,k+1):
    for b in range(a+1,k+1):
        for c in range(b+1,k+1):
            li = [a,b,c]
            wa += reduce(math.gcd,li)*6

for a in range(1,k+1):
    for b in range(a+1,k+1):
        wa += math.gcd(a,b)*6

for a in range(1,k+1):
    wa += a
    

print(wa)
