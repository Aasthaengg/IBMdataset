import sys
input = sys.stdin.readline
import math

def INT(): return int(input())
def MAPINT(): return map(int, input().split())
def LMAPINT(): return list(map(int, input().split()))
def STR(): return input()
def MAPSTR(): return map(str, input().split())
def LMAPSTR(): return list(map(str, input().split()))

f_inf = float('inf')

x, n = LMAPINT()
if n == 0:
  _ = input()
  print(x)
  exit()

p = LMAPINT()
for i in range(100):
  if (x-i) not in p:
    print(x-i)
    exit()
  if (x+i) not in p:
    print(x+i)
    exit()