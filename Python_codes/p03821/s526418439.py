import sys
import numpy as np
input = sys.stdin.readline

N = int(input())
A = []
B = []
for _ in range(N):
    a,b = list(map(int,input().split()))
    A.append(a)
    B.append(b)
cnt = 0
for i in range(N-1,-1,-1):
    if (A[i]+cnt)%B[i] == 0:
        continue
    else:
        cnt += B[i] - (A[i]+cnt)%B[i]
print(cnt)
