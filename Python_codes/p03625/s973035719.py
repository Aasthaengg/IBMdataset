from collections import *
N = int(input())
C = Counter(map(int,input().split()))
A = [0,0]
B = [0]

for k,v in C.items():
  if 2<=v:
    A+=[k]
  if 4<=v:
    B+=[k]

A.sort()
B.sort()
print(max(A[-1]*A[-2],B[-1]**2))