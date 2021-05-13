import sys
import heapq
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

A = sum(map(int,input().split()))
if A < 22:
    print("win")
else:
    print("bust")