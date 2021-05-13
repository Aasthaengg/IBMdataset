a = list(map(str,(input())))
b = list(map(str,(input())))
c = list(map(str,(input())))
 
card = a[0]
 
for i in range(len(a) + len(b) + len(c)):
    if card == 'a':
        if a == []:
            print("A")
            break
        else:
            card = a[0]
            a.pop(0)
 
    elif card == 'b':
        if b == []:
            print("B")
            break
        else:
            card = b[0]
            b.pop(0)
 
    else:
        if c == []:
            print("C")
            break
        else:
            card = c[0]
            c.pop(0)