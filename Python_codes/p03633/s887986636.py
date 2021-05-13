import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

from fractions import gcd

N = int(input())

T = int(input())

for _ in range(N - 1):
    t = int(input())
    T = T * t // gcd(T, t)

print (T)