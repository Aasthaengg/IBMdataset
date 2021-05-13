result = []
while True:
    a,op,b = input().split()
    
    if op == '?':
        break
    elif op == '+':
        result.append(int(a) + int(b))
    elif op == '-':
        result.append(int(a) - int(b))
    elif op == '*':
        result.append(int(a) * int(b))
    elif op == '/':
        result.append(int(int(a) / int(b)))
        
for i in result:
    print(i)