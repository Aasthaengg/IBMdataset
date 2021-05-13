from sys import stdin
from math import gcd

def input():
    return stdin.readline().strip()

n = int(input())
l = [int(input()) for _ in range(n)]

now = l[0]
for i in range(1, n):
    now = now * l[i] // gcd(now, l[i])

print(now)