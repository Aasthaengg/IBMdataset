X, K, D = map(int, input().split())

X = abs(X)

if K * D < X:
    print(X - K * D)

else:
    cnt = (X - X%D) // D
    if (K-cnt)%2==0:
        print(X%D)
    else:
        print(D - X%D)
