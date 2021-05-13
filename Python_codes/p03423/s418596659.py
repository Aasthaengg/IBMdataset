from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solve():
  n = int(input())
  print(n//3)
solve()