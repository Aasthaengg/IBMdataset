import sys
from collections import defaultdict, deque
import bisect
from heapq import *
from math import factorial
sys.setrecursionlimit(200000)
input = sys.stdin.readline

# N, W, = map(int, input().split())
# N = int(input())
# L = [int(v) for v in input().split()]
# L = [[int(v) for v in input().split()] for _ in range(N)]
# L = [int(input()) for _ in range(N)]
# L = [list(input().strip())  for _ in range(N)]
S = input().strip()

q = deque(S)
c = 0
while len(q):
     l = q[0]
     r = q[len(q)-1]

     if l == r:
          if len(q) != 1:
               q.pop()
          q.popleft()
     elif l == 'x':
          q.append('x')
          c += 1
     elif r == 'x':
          q.appendleft('x')
          c += 1
     else:
          print(-1)
          exit()

print(c)
