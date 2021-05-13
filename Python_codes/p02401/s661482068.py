#coding : utf-8
while True:
    aa, op, bb = input().split()
    if op == '?':
        break
    a = int(aa)
    b = int(bb)
    if op == '+':
        print (a+b)
    elif op == '-':
        print (a-b)
    elif op == '*':
        print (a*b)
    elif op == '/':
        print (a//b)
