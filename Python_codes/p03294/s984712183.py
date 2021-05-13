import sys
input = sys.stdin.readline
from collections import *

N = int(input())
a = list(map(int, input().split()))
print(sum(a)-N)