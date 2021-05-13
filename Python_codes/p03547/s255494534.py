def actual(x, y):
    ord_x = ord(x)
    ord_y = ord(y)
    
    if ord_x < ord_y:
        return '<'

    if ord_x > ord_y:
        return '>'

    return '='

x, y = input().split()
print(actual(x, y))
