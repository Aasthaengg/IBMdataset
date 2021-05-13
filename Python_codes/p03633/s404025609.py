from functools import reduce
from math import gcd
N = int(input())
T = 0
for i in range(N):
    if not T:
        T = int(input())
    else:
        t = int(input())
        T = T*t//gcd(T,t)
print(T)