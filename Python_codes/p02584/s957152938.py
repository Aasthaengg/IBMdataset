X, K, D = map(int, input().split())

X = abs(X)
if X % D == 0:
    tmp = X // D
    if tmp >= K:
        print(X - D * K)
    else:
        tmp = K - tmp
        if tmp % 2 == 0:
            print(0)
        else:
            print(D)
else:
    tmp = X // D
    if tmp >= K:
        print(X - D * K)
    else:
        tmp = K - tmp
        if tmp % 2 == 0:
            print(X - X // D * D)
        else:
            print(abs(X - (X // D + 1) * D))