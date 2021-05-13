import sys
d={}
for e in sys.stdin.readlines()[1:]:
 if'i'==e[0]:d[e[7:]]=0
 else:print(['no','yes'][e[5:]in d])
