A = []
B = []
C = []

for i in range(1,101):
    t0 = i
    t1 = i*100
    t2 = i*100*100
    A.append(t0)
    B.append(t1)
    C.append(t2)

d,n = map(int,input().split())

if d == 0:
    if n == 100:
        print(101)
    else:
        print(A[n-1])
elif d == 1:
    if n == 100:
        print(100*101)
    else:
        print(B[n-1])
else:
    if n == 100:
        print(100*100*101)
    else:
        print(C[n-1])