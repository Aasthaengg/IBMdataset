import sys
  
for s in sys.stdin:
    m,n = map(int,s.split())
    g,r = m,n
    while r!=0:
      g,r = r,g%r
    print(g,m//g*n)