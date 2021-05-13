x, y = [int(i, 16) for i in input().split()]

if x < y:
    print("<")
elif x > y:
    print(">")
else:
    print("=")