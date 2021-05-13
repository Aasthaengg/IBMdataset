import sys
import heapq
from decimal import Decimal

input = sys.stdin.readline

n, k, q = map(int, input().split())
point_list = [0]*n
S = []

for _ in range(q):
    ai = int(input())
    point_list[ai-1] += 1

for point in point_list:
    if k - (q - point) > 0:
        print("Yes")
    else:
        print("No")
