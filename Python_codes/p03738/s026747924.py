
a = int(input())
b = int(input())

if len(str(a)) > len(str(b)):
    print("GREATER")
elif len(str(a)) < len(str(b)):
    print("LESS")
else:
    if a > b:
        print("GREATER")
    elif a < b:
        print("LESS")
    else :
        print("EQUAL")
