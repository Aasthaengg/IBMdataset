# 初期入力
import numpy as np
import sys
input = sys.stdin.readline
N,M,C = (int(i) for i in input().split())
B = list(map(int, input().split()))
B =np.array(B,dtype=int)
A =np.zeros((N,M),dtype=int)
for i in range(N):
    A[i] = list(map(int, input().split()))
    
#
count =0
for i in range(N):
    if np.sum(A[i] *B) +C >0:
        count +=1
print(count) 