a,b = map(str,input().split())

if a == "A":
    a = 10
elif a == "B":
    a = 11
elif a == "C":
    a = 12
elif a == "D":
    a = 13
elif a == "E":
    a = 14
else:
    a = 15

if b == "A":
    b = 10
elif b == "B":
    b = 11
elif b == "C":
    b = 12
elif b == "D":
    b = 13
elif b == "E":
    b = 14
else:
    b = 15

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")