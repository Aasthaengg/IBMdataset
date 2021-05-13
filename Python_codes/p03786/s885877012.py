# coding: utf-8
import bisect
import math
#N, c, k = map(int,input().split())
N = int(input())
#T = []
A = list(map(int,input().split()))
A.sort()
A_ = sorted(A)
ans = 0
for i in range(N-1):
    A_[i+1] += A_[i]
#print(A)
#print(A_)
t=0
for i in range(N-1):
    #print(ans)
    if A_[i]*2 >= A[i+1]:
        ans += 1
    else:
        ans = 0
ans += 1
print(ans)