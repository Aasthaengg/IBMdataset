x, y = map(str, input().split())
ord_x = ord(x)
ord_y = ord(y)

if ord_x > ord_y:
    print('>')

elif ord_x < ord_y:
    print('<')

else:
    print('=')