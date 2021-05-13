X, K, D = map(int, input().split())

absX = abs(X)
a = absX - K * D
minX = absX % D

if a > 0:
    print(a)

elif a <= 0:

    Kmin = (absX - minX) / D
    Krem = K - Kmin

    if Krem % 2 == 0:
        print(min(abs(minX), abs(minX - 2 * D)))
    else:
        print(min(abs(minX + D), abs(minX - D)))
