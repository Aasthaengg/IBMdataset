a,op,b = map(str,input().split())
while op != '?':
    a = int(a); b = int(b);
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a//b)
    a,op,b = map(str,input().split())

