X, K, D = map(int, input().split())
X = abs(X)

if X-D*K>=0:
    print(X-D*K)
else:
    p = X%D
    c = (X-p)//D
    
    if (K-c)%2==0:
        print(p)
    else:
        print(-(p-D))