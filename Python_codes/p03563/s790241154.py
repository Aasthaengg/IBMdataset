import sys
from itertools import accumulate
input = sys.stdin.readline
def inputs():return [int(x) for x in input().split()]
R = int(input())
G = int(input())
print(2*G-R)