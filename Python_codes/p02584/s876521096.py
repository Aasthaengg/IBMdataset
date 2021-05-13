X, K, D = list(map(int, input().split()))

if X < 0:
    X = -X

if X > K * D:
    print(X - K * D)
else:
    count = X // D
    coodinate = X - count * D
    if (K - count) % 2 == 0:
        print(coodinate)
    else:
        print(D - coodinate)