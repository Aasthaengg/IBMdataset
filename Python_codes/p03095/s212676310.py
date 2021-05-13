from string import ascii_lowercase
from functools import reduce
from operator import mul
n = int(input())
S = input()
mod = 10**9 + 7
print(reduce(lambda x, y: x*y % mod, (S.count(c)+1 for c in ascii_lowercase))-1)