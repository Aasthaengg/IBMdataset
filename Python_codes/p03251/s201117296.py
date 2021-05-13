n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
# (max(x), min(y)] & (X, Y]
print('No War' if max(X, max(x)) < min(Y, min(y)) else 'War')
