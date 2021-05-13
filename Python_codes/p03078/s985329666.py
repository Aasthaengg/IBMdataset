X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
D = []
for i in range(X):
    for j in range(Y):
        for k in range(Z):
            if i * j * k > K:
                break
            D.append(A[i] + B[j] + C[k])
D.sort(reverse=True)
for d in D[:K]:
    print(d)
