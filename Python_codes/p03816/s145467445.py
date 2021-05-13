import sys
from heapq import heapify, heappop, heappush
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = IL()

seta = set(a)
num = N - len(seta)

if num%2 == 0:
  print(N - num)
else:
  print(N - (num + 1))