import math
n = int(input())
A = list(map(int,input().split()))

L = 2
R = 2
k = 0
for i in range(n):
    if L//A[n-1-i] == R//A[n-1-i] and L % A[n-1-i] != 0:
        k = 1
        break
    else:
        L = (math.ceil(L/A[n-1-i]))*A[n-1-i]
        R = (R//A[n-1-i]+1) * A[n-1-i] - 1
print(L,R) if k == 0 else print("-1")