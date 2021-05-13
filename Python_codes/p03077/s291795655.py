import sys
input = sys.stdin.readline
from math import ceil
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

X = min([A, B, C, D, E])
ans = ceil(N/X) + 4
print(ans)