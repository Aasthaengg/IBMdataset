i = 1

while i == 1:
    x = raw_input()
    a, op, b = x.split(" ")
    a = int(a)
    b = int(b)
    
    if op == "?":
        i = 0
    elif op == "+":
        print ("%d" %(a+b))
    elif op == "-":
        print ("%d" %(a-b))
    elif op == "*":
        print ("%d" %(a*b))
    else:
        print("%d" %(a/b))