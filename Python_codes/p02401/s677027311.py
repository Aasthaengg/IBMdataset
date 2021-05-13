ss = input("").split()
a = int(ss[0])
b = ss[1]
c = int(ss[2])

while b != "?":
    if b == "+":
        result = int(a + c)
    elif b == "-":
        result = int(a - c)
    elif b == "*":
        result = int(a * c)
    elif b== "/":
        result = int(a / c)

    print("{0}".format(result))
    ss = input("").split()
    a = int(ss[0])
    b = ss[1]
    c = int(ss[2])