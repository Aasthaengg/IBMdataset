X, K, D = map(int, input().split())
if X < 0:
    X = -X
step = X//D
X -= D*step
K -= step

if K <= 0:
    print(X-K*D)
    exit()
if K % 2 == 0:
    print(X)
else:
    print(abs(X-D))
