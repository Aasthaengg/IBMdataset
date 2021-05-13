import math
 
N = int(input())
C = [int(input()) for i in range(5)]
 
M = 4
W = math.ceil(N/min(C))
 
print(M+W)