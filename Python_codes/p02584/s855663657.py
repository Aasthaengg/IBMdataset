X, K, D = map(int, input().split())

if X == 0:
    print(0 if K % 2 == 0 else D)
elif X < 0:

    div = abs(X) // D
    tmp = X + D*div

    if div >= K:
        print(abs(X + D*K))
    elif div < K:
        K -= div
        print(abs(tmp) if K % 2 == 0 else abs(tmp+D))    

else:

    div = abs(X) // D
    tmp = X - D*div

    if div >= K:
        print(abs(X - D*K))
    elif div < K:
        K -= div
        print(abs(tmp) if K % 2 == 0 else abs(tmp-D))


