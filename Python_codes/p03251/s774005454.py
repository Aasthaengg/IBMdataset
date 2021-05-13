n, m, X, Y = map(int, input().split())
x = max(map(int, input().split()))
x = max(X, x)
y = min(map(int, input().split()))
y = min(Y, y)
if x < y:
    print('No War')
else:
    print('War')
