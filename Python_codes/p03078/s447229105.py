def resolve():
    X, Y, Z, K = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)

    ABC = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if ((i+1)*(j+1)*(k+1) > K):
                    break
                ABC.append(A[i]+B[j]+C[k])
    ABC = sorted(ABC, reverse=True)
    [print(ABC[i]) for i in range(K)]

if '__main__' == __name__:
    resolve()