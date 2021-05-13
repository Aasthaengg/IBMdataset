n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
x_max = x[-1]
y_min = y[0]
if max(X, x_max) < min(Y, y_min):
    print('No War')
else:
    print('War')