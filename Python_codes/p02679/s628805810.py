import sys
import math
from math import gcd

mod = 1000000007
 
N = int(sys.stdin.readline().strip())
zero = 0
mp = {}
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())

    if a == 0 and b == 0:
        zero += 1
        continue
 
    g = gcd(a, b)
    a = a // g
    b = b // g
 
    if b < 0:
        a = -a
        b = -b
    if b == 0 and a < 0:
        a = -a
    if a <= 0:
        a, b = b, -a
        if (a, b) in mp:
            mp[(a, b)][0] += 1
        else:
            mp[(a, b)] = [1, 0]
    else:
        if (a, b) in mp:
            mp[(a, b)][1] += 1
        else:
            mp[(a, b)] = [0, 1]
 
ans = 1
for key in mp:
    s, t = mp[key]
    ans *= pow(2, s, mod) + pow(2, t, mod) - 1
    ans %= mod
print((zero - 1 + ans) % mod)