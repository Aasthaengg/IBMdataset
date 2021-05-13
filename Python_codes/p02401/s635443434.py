
for i in range(1000):
    
    a, b, c = input().split()
    
    if b == '?': break
    
    a = int(a)
    c = int(c)
    
    if b == '+': print(a + c)
    if b == '-': print(a - c)
    if b == '*': print(a * c)
    if b == '/': print(int(a / c))





