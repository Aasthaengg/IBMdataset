import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
N, M, X = map(int, input().split())
a = list(map(int, input().split()))
x = bl(a, X)
print(min(x, M - x))