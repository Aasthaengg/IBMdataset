a, b, c = map(int, input().split())
X = max([a, b, c])
if (X == a+b+c-X):
    print('Yes')
else:
    print('No')
