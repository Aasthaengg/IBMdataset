#!/usr/bin/env python

sa = input()
sb = input()
sc = input()

ch = sa[0]
sa = sa[1:]

while True:
    if ch == 'a':
        if len(sa) == 0:
            print('A')
            exit()
        ch = sa[0]
        sa = sa[1:]
    elif ch == 'b':
        if len(sb) == 0:
            print('B')
            exit()
        ch = sb[0]
        sb = sb[1:]
    elif ch == 'c':
        if len(sc) == 0:
            print('C')
            exit()
        ch = sc[0]
        sc = sc[1:]
