X, Y = map(str, input().split())
lst = ["A","B","C","D","E","F"]
x = lst.index(X)
y = lst.index(Y)

if x < y:
    print("<")
elif x > y:
    print(">")
else:
    print("=")