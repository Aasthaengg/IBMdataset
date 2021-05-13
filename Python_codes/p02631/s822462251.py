import array
from functools import reduce
from operator import xor

N = int(input())
A = array.array("L", map(int, input().split()))

Q = array.array("L", [0]) * N

R = reduce(xor, A)
for i in range(N):
    print(R^A[i])
