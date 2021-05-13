import sys
input = sys.stdin.readline
from collections import *

A, B, C = map(int, input().split())

if A<=C<=B:
    print('Yes')
else:
    print('No')