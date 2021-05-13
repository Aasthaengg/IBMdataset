import sys
input = sys.stdin.readline
from collections import *

S = list(input()[:-1])
S[3] = '8'
print(''.join(S))