X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
P = []
for i in range(min(3000, X)):
    for j in range(min(3000//(i+1) + 1, Y)):
        for z in range(min(3000//(i+1)//(j+1) +1, Z) ):
            P.append(A[i]+B[j]+C[z])
P.sort(reverse=True)
for i in range(K):
    print(P[i])