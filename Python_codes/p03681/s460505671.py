import sys
import math
def kaijyo(n):
  return math.factorial(n)%(10**9+7)
N,M=map(int,input().split())
if abs(N-M)>1:
  print(0)
  sys.exit()
if N-M==-1:
  N,M=M,N
if N-M==1:
  print((kaijyo(N)*kaijyo(M))%(10**9+7))
  sys.exit()
else:
  print((2*kaijyo(N)*kaijyo(M))%(10**9+7))
  sys.exit()