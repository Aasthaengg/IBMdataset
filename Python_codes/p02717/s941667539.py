X, Y, Z = [int(i) for i in input().split()]
temp = int()
temp = Y
Y = X
X= temp
temp = Z
Z = X
X = temp
print(X, Y, Z)