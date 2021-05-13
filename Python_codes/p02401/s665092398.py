while True:
    table= input().split()
    
    a = int(table[0])
    op = table[1]
    b = int(table[-1])
    
    if op == '?':
        break
        
    if op == '+':
        print(a+b)
    elif op =='-':
        print(a-b)
    elif op =='*':
        print(a*b)
    else:
        print(a//b)
    
    
