n, m, X, Y = map(int, input().split())
x = [int(i) for i in input().split()] + [X]
y = [int(i) for i in input().split()] + [Y]
if max(x) < min(y):
    print('No War')
else:
    print('War')