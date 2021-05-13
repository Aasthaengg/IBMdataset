N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
import math

if N%min(A,B,C,D,E) ==0:
  print(5 + N//min(A,B,C,D,E)-1)
else:
  print(5+N//min(A,B,C,D,E))