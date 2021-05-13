# -*- coding: utf-8 -*-

w, h, x, y = map(int, input().split())

def multi(w, h, x, y):
    core = (w/2, h/2)
    if (x == core[0])^(y == core[1]):
        return False
    elif x == core[0]:
        return True
    else:
        return False

print(w*h/2, 1 if multi(w, h, x, y) else 0)
