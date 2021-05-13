while True :
    a, op, b = map(str, raw_input().split(" "))
    a = int(a)
    b = int(b)
    if (op == "?") :
        break
    elif (op == "+") :
        print("%d" % (a+b))
    elif (op == "-") :
        print("%d" % (a-b))
    elif (op == "*") :
        print("%d" % (a*b))
    elif (op == "/") :
        print("%d" % (a/b))