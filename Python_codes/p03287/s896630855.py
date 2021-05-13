import collections
import numpy as np

N,M = map(int,input().split())
A=np.array([0]+[int(x) for x in input().split()])
B=np.mod(A.cumsum(),M)
answer=0
C = collections.Counter(B)

for x in C.values():
  answer += x*(x-1)//2
print(answer)