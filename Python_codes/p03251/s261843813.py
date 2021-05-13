N, M, X, Y = map(int, input().split())
x = [int(i) for i in input().split()]
x.append(X)
y = [int(i) for i in input().split()]
y.append(Y)

if max(x) < min(y):
    print('No War ')
else:
    print('War')