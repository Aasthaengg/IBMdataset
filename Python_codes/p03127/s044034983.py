import sys
from math import gcd
input = sys.stdin.readline
N = int(input())
res = 0
a = list(map(int, input().split()))
for x in a: res = gcd(res, x)
print(res)