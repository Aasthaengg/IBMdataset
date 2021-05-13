s = raw_input()
nlist = map(int, s.split())
a, b, c= nlist

if a<b:
    if b<c:
        print '%d %d %d' %(a, b, c)
    elif c<a:
        print '%d %d %d' %(c, a, b)
    else:
        print '%d %d %d' %(a, c, b)
else:
    if a<c:        
        print '%d %d %d' %(b, a, c)
    elif c<b:
        print '%d %d %d' %(c, b, a)
    else:
        print '%d %d %d' %(b, c, a)