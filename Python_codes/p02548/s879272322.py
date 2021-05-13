import sys
import math
 
input = sys.stdin.readline
 
N = int(input())
 
total = 0
for i in range(1, N):
    total += (N-1) // i
 
print(total)