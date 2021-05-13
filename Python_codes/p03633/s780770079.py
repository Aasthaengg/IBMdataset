from math import gcd
import sys

def lcm(a, b):
    return a * b // gcd(a, b)

N = int(input())
T = [int(input()) for _ in range(N)]

if N == 1:
    print(T[0])
    sys.exit()

l = lcm(T[0], T[1])
for i in range(2, N):
    l = lcm(l, T[i])

print(l)