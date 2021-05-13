while True:
    a, op, b = raw_input().split()
    a, b = map(int,[a,b])
    if op == "?":
        break
    if op=="+":
        print (a+b)
    elif op=="-":
        print (a-b)
    elif op=="*":
        print (a*b)
    elif op=="/":
        print (a/b)