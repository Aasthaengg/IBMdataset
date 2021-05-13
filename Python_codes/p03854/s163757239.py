# -*- coding: utf-8 -*-

S = input()

words = ['dream', 'dreamer', 'erase', 'eraser']

while len(S)>0:
    hit = False
    for w in words:
        s = S[-len(w):]
        if w == s:
            S = S[0:-len(w)]
            hit = True
            break
    
    if not hit:
        break

if len(S)==0:
    print('YES')
else:
    print('NO')
