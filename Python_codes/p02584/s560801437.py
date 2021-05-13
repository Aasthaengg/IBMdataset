X, K, D = map(int, input().split())

c = abs(X) // D
k = min(c, K)
K -= k
if K == 0:
    if X > 0:
        print(abs(X-D*k))
        exit()
    elif X < 0:
        print(abs(X+D*k))
        exit()

if X > 0:
    X -= D*k
    if abs(X-D) < abs(X):
        X -= D
        K -= 1
elif X < 0:
    X += D*k
    if abs(X+D) < abs(X):
        X += D
        K -= 1

if K % 2 == 0:
    print(abs(X))
else:
    print(min(abs(X-D), abs(X+D)))
