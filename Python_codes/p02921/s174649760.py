import sys
input = sys.stdin.readline
from collections import *

S = input()[:-1]
T = input()[:-1]
ans = 0

for i in range(3):
    if S[i]==T[i]:
        ans += 1

print(ans)