#!/usr/bin/env python3
import collections
import itertools as it
import math
#import numpy as np

#  = int(input())
n, m = map(int, input().split())
s = input()
t = input()
#  = list(map(int, input().split()))
#  = [int(input()) for i in range(N)]
#
# c = collections.Counter()
#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

g = gcd(n, m) 
a = n // g
b = m // g
for i in range(g):
    if s[i*a] != t[i*b]:
        print(-1)
        break
else:
    print(n * m // g)
