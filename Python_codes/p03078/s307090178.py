X,Y,Z,K = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

D = []
for i in range(X):
    for j in range(Y):
        D.append(A[i]+B[j])
D.sort(reverse=True)

E = []
for i in range(min(len(D),K)):
    for j in range(Z):
        E.append(D[i]+C[j])
E.sort(reverse=True)

for i in range(K):
    print(E[i])