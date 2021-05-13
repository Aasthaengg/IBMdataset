n, m, x, y = map(int, input().split())
X = [int(i) for i in input().split()]
Y = [int(i) for i in input().split()]

X.append(x)
Y.append(y)

X.sort()
Y.sort()

print('War' if max(X) >= min(Y) else 'No War')