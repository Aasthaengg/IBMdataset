import math
N,H = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
a = 0
for i in range(N):
    if A[i][0]>a:
        a = A[i][0]
B = []
for i in range(N):
    if A[i][1]>a:
        B.append(A[i][1])
B = sorted(B,reverse=True)
totB = sum(B)
if totB>=H:
    flag = 0
    tot = 0
    for i in range(len(B)):
        tot += B[i]
        if tot>=H:
            flag = i+1
            break
    print(flag)
else:
    h = H-totB
    n = len(B)+math.ceil(h/a)
    print(n)