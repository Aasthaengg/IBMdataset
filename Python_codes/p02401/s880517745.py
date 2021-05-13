
while True:
    a,op,b = input().split()
    if(op == '+'):
        print(int(a)+int(b))
    elif(op == '-'):
        print(int(a)-int(b))
    elif(op == '*'):
        print((int(a)*int(b)))
    elif(op == '/'):
        print('%d'%(int(a)/int(b)))
    elif(op == '?'):
        break;
            

