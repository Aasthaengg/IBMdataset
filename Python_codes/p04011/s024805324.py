N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if K < N:
    x = X*K + Y*(N-K)
    print(x)
else:
    x = N*X
    print(x)