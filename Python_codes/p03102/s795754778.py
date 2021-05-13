def f(A,B,C,M):
    X=C
    for i in range(M):
        X+=A[i]*B[i]
    return X

K=0
N,M,C=map(int,input().split())
B=list(map(int,input().split()))
for _ in range(N):
    A=list(map(int,input().split()))
    K+=f(A,B,C,M)>0
print(K)
