from collections import *
N = int(input())
C = Counter([int(input()) for n in range(N)]) 
A = [1 for v in C.values() if v%2==1]
print(sum(A))