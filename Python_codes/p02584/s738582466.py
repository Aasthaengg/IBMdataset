X, K, D = [int(x) for x in input().split()]

X = abs(X)

straight = min(K, X // D)

K -= straight;
X -= straight * D;

if K % 2 == 0:
    print(X)
else:
    print(D - X)
