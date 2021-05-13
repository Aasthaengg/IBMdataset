import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
A = list(map(int, input().split()))
G = 0

for Ai in A:
    G = gcd(G, Ai)

print(G)