import math

X,K,D = map(int,input().split())

X = abs(X)

if X//D > K:
    ans = X - D*K
    print(abs(ans))
elif (K-(X//D))%2 == 0:
    Y = X - (X//D)*D
    print(abs(Y))
else:
    Y = X - (X//D)*D
    print(abs(D-Y))
