matrix = []
while True:
    values = input()
    if '?' in values:
        break
    matrix.append([x for x in values.split()])
    
for a, op, b in matrix:
    if '+' == op:
        print(int(a) + int(b))
    elif '-' == op:
        print(int(a) - int(b))
    elif '*' == op:
        print(int(a) * int(b))
    elif '/' == op:
        print(int(a) // int(b))
    else:
        pass