#Sequence Growing Easy

import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for i in range(N)]

judge = 1
for i in range(N):
    if i != N-1:
        if A[i+1] <= A[i]+1 and A[i] <= i:
            pass
        else:
            judge = 0
    else:
        if A[i] <= i:
            pass
        else:
            judge = 0

if judge == 0:
    print(-1)
else:
    n = 1
    if A[N-1] == 0:
        n = 0
    for i in range(N-1):
        if A[(N-2)-i] == 0:
            n = n
        elif A[(N-2)-i] < A[(N-1)-i] and A[(N-2)-i] != 0:
            n = n + 1
        elif A[(N-2)-i] == A[(N-1)-i] and A[(N-2)-i] != 0:
            n = n + A[(N-2)-i]
        elif A[(N-2)-i] > A[(N-1)-i] and A[(N-1)-i] != 0:
            n = n + A[(N-1)-i]
        else:
            n = n + 1
    print(int(n))