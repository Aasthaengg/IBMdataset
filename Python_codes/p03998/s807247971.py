# -*- coding: utf-8 -*-

sa = list(str(input()))
sb = list(str(input()))
sc = list(str(input()))

t = 'a'
winner = ''

while True:
    if t == 'a':
        if len(sa) == 0:
            winner = 'A'
            break  
        t = sa.pop(0)
    elif t == 'b':
        if len(sb) == 0:
            winner = 'B'
            break  
        t = sb.pop(0)
    else:
        if len(sc) == 0:
            winner = 'C'
            break  
        t = sc.pop(0)

print(winner)