while True:
    line = input().split()
    if line[1]=='?': break
    a, b, op = int(line[0]),int(line[2]),line[1]
    if op=='+': result = a+b
    elif op=='-': result = a-b
    elif op=='*': result = a*b
    elif op=='/': result = a//b
    print(result)