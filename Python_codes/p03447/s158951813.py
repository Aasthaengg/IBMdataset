X = int(input())
A = int(input())
B = int(input())

X = X - (A + B * ((X - A) // B))
print(X)