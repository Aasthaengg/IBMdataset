import sys
for e in sys.stdin:
 g,d=a,b=list(map(int,e.split()))
 while d:g,d=d,g%d
 print(g,a*b//g)
