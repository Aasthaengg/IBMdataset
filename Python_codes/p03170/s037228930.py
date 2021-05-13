import math
import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,K = IL()
a = IL()

dp = [-1]*200010
for i in a:
  dp[i] = True

for i in range(1,K+1):
  if dp[i] == -1 or dp[i] == False:
    dp[i] = False
    for j in a:
      dp[i+j] = True

if dp[K] == True:
  print("First")
else:
  print("Second")