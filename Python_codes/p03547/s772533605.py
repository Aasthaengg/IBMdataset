X, Y = input().split()
X = int(X, base=16)
Y = int(Y, base=16)
if X > Y:
    print(">")
elif X == Y:
    print("=")
else:
    print("<")