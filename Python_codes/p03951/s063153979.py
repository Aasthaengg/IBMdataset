import sys
input = sys.stdin.readline
from collections import *

N = int(input())
s = input()[:-1]
t = input()[:-1]

for match in range(N, 0, -1):
    if s[N-match:]==t[:match]:
        print(2*N-match)
        exit()

print(2*N)