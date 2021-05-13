# -*- coding: utf-8 -*-
import sys
from itertools import permutations 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = list(map(int,readline().split()))

x = max(A)
x_ind = A.index(x)
y = min(A)
y_ind = A.index(y)

if x >= 0 and y >= 0:
    print(N-1)
    for i in range(1,N):
        print(i,i+1)
elif x <= 0 and y <= 0:
    print(N-1)
    for i in range(N-1,0,-1):
        print(i+1,i)
else:
    cnt = N-1
    ans = []
    if abs(x) >= abs(y):
        for i in range(N):
            if A[i] < 0:
                cnt += 1
                ans.append((x_ind+1,i+1))
        for i in range(1,N):
            ans.append((i,i+1))
    else:
        for i in range(N):
            if A[i] > 0:
                cnt += 1 
                ans.append((y_ind+1,i+1))
        for i in range(N-1,0,-1):
            ans.append((i+1,i))
    print(cnt)
    for x,y in ans: 
        print(x,y)