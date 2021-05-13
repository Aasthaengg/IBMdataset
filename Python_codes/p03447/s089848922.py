X = int(input())
A = int(input())
B = int(input())

X = X - A

for i in range(100):
    if X - B >= 0:
        X = X - B

print(X)
