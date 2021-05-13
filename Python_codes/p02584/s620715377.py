X, K, D = map(int,input().split())
X = abs(X)
T = X//D
if K < T:
    print(X-K*D)
else:
    X -= T*D
    K -= T
    if K&1:
        print(D-X)
    else:
        print(X)