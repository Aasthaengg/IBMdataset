from itertools import accumulate
from bisect import *
N, X = map(int, input().split())
L = list(map(int, input().split()))
S = list(accumulate([0]+L))
print(bisect_right(S,X))