X, Y = list(map(str, input().split()))

if X < Y:
    print("<")
elif X == Y:
    print("=")
else:
    print(">")