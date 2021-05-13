from functools import reduce
from operator import xor

n = int(input())
aaa = list(map(int, input().split()))
print('YES' if reduce(xor, aaa) & 1 == 0 else 'NO')
