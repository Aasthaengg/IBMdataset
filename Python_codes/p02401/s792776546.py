while(True):
    hoge = input().split()
    a = int(hoge[0])
    b = int(hoge[2])
    op = hoge[1]
    if(op == '+'):
        ans = a + b
    elif(op == '-'):
        ans = a - b
    elif(op == '*'):
        ans = a * b
    elif(op == '/'):
        ans = int(a / b)
    else:
        exit()
    print(ans)