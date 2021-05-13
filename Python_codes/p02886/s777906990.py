from functools import reduce
from itertools import accumulate
from math import gcd
n=int(input())
L=list(map(int,input().split()))
print(sum(d*cumulate for d,cumulate in zip(L[1:],accumulate(L))))
