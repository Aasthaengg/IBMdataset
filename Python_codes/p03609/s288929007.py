def actual(X, t):
    if X <= t:
        return 0

    return X - t

X, t = map(int, input().split())
print(actual(X, t))