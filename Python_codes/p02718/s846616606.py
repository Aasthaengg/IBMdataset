import math
N,M = map(int,input().split())
A = list(map(int,input().split()))
a = sum(A)
b = math.ceil(a/(4*M))
cnt = 0
for i in range(N):
    if A[i]>=b:
        cnt += 1
if cnt>=M:
    print("Yes")
else:
    print("No")