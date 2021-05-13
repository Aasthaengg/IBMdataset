X,K,D = map(int, input().split())
X = abs(X)
if K*D <= X:
    print(X-K*D)
else:
    tempK = X//D
    if (K-tempK)%2==0:
        print(X-D*tempK)
    else:
        print(abs(X-D*tempK-D))
