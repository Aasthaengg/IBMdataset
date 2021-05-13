import sys
from collections import defaultdict
sys.setrecursionlimit(200000)
input = sys.stdin.readline

A, B, C, D, = map(int, input().split())

if abs(B - A) <= D and abs(C - B) <= D:
    print("Yes")
elif abs(C - A) <= D:
    print("Yes")
else:
    print("No")