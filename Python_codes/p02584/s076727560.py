X, K, D = map(int, input().split())

XX = abs(X)

if XX > K*D:
    print(XX - K*D)
else:
    if (K - X//D)%2 == 0:
        print(X%D)
    else:
        print(abs(X%D -D))

