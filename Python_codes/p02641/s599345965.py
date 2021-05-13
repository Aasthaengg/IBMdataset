X,N= map(int,input().split())
P = list(map(int,input().split()))
a = range(X-101,X,1)
a1 = sorted(a,reverse=True)
b = range(X,X+101,1)
A = []
B = []
for i in range(len(a1)):
    C = a1[i] not in P
    if C==True:
        A.append(a1[i])
    else:
        continue
for i in range(len(b)):
    D = b[i] not in P
    if D==True:
        B.append(b[i])
    else:
        continue
if X-A[0] <= B[0]-X:
    print(A[0])
else:
    print(B[0])