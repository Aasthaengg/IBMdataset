while True:
    v = raw_input()
    a = v.split(' ')
    if a[1] == "?":
        break
    if a[1] == "+":
        print int(a[0]) + int(a[2])
    elif a[1] == "-":
        print int(a[0]) - int(a[2])
    elif a[1] == "*":
        print int(a[0]) * int(a[2])
    elif a[1] == "/":
        print int(a[0]) / int(a[2])