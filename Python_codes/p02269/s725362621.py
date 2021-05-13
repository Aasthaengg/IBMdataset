import sys
d=set()
input()
for e in sys.stdin:
 c,g=e.split()
 if'i'==c[0]:d|=set([g])
 else:print(['no','yes'][g in d])
