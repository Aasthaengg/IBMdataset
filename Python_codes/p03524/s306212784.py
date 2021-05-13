import sys
input = sys.stdin.readline
from collections import *

S = input()[:-1]
a = S.count('a')
b = S.count('b')
c = S.count('c')

if max(a, b, c)-min(a, b, c)<=1:
    print('YES')
else:
    print('NO')