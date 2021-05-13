while 1:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    if a == -1 or b == -1 or a + b < 30:print('F')
    elif a + b >= 80:print('A')
    elif a + b >= 65: print('B')
    elif a + b >= 50:print('C')
    elif a + b >= 30 and c >= 50:print('C')
    else:print('D')
    
    
