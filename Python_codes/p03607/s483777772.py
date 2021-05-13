from collections import *
N = int(input())
C = Counter([int(input()) for n in range(N)])
print(sum(v%2==1 for v in C.values()))