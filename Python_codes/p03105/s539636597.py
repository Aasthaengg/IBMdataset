import sys
input = sys.stdin.readline
from collections import *

A, B, C = map(int, input().split())
print(min(C, B//A))