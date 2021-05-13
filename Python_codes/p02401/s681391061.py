while 1:
        i  =  raw_input().split()
        a = int(i[0])
        op = i[1]
        b = int(i[2])

        if op == "+":
                x = a+b
        elif op == "-":
                x = a-b
        elif op == "*":
                x = a*b
        elif op == "/":
                x = a/b
        elif op == "?":
                break
        print  x