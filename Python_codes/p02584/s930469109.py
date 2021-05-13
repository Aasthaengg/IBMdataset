X,K,D = [int(x) for x in input().split()]

if D * K < abs(X):
    print(abs(X) - D * K)
else:
    if (K - abs(X) // D) % 2 == 0:
        print(abs(X) % D)
    else:
        print(D - abs(X) % D)