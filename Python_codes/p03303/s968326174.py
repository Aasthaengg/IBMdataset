import sys
input = sys.stdin.readline
from collections import *

S = input()[:-1]
w = int(input())
ans = ''

for i in range(0, len(S), w):
    ans += S[i]

print(ans)