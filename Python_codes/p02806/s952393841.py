import sys
import fractions
import math
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
st = [SL() for i in range(N)]
g = S()
#print(st)

f = 0
ans = 0
for s,t in st:
  if f == 0:
    if s == g:
      f = 1
  else:
    ans += int(t)
print(ans)