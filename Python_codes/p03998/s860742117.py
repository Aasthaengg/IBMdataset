a = list(input())
b = list(input())
c = list(input())
st = a.pop(0)
while True:
    if st == 'a':
        if a == []:
            print('A')
            break
        else:
            st = a.pop(0)
    elif st == 'b':
        if b == []:
            print('B')
            break
        else:
            st = b.pop(0)
    else:
        if c == []:
            print('C')
            break
        else:
            st = c.pop(0)