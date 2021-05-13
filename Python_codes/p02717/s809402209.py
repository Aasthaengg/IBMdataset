X, Y, Z = map(int, input().split())
temp = X
X = Y
Y = temp
temp = X
X = Z
Z = temp
print(X, Y, Z)