X, K, D = map(int, input().split())

X = abs(X)

cuts = X//D

if cuts>=K:
    print(X-(K*D))
else:
    remainingcuts = K-cuts
    r = X-cuts*D

    if remainingcuts%2 == 1:
        print(abs(r-D))
    else:
        print(r)
