while 1:
    a,op,b=input().split()
    if op == '+':
        r = int(a)+int(b)
    elif op == '-':
        r = int(a)-int(b)
    elif op == '*':
        r = int(a)*int(b)
    elif op == '/':
        r = int(a)//int(b)
    elif op == '?':
        break;
    print(r)