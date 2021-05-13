import itertools
import math

N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
n=0
A_list=itertools.permutations(range(1,N+1))
for A in A_list:
  n+=1
  A=list(A)
  if A==P:
    a=n
  if A==Q:
    b=n

print(abs(a-b))

