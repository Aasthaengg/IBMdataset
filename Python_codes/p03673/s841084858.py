N=int(input())
A=list(map(int,input().split()))

X=[A[i] for i in range(0,N,2)]
Y=[A[i] for i in range(1,N,2)]

if N%2:
    A=X[::-1]
    B=Y
else:
    A=Y[::-1]
    B=X

print(" ".join(map(str,A+B)))
