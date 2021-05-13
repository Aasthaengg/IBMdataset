import math 
N = int(input())
A = map(int,input().split())
B = map(bin,A)
def Y(x):
  y = len(x)-x.rfind("1")-1
  return y
C = map(Y,B)
print(min(C))
