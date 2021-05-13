import sys
a1 = []
for l in sys.stdin:
    a1.append(int(l))
a, b , c ,d = tuple(a1)
print( min([a , b]) + min([c , d ]))