import sys
a=sys.stdin.readline()
res = [int(i) for i in a.split() if i.isdigit()] 
r,D,x2000 = [res[i] for i in (0,1,2)]
if (r>=2 and r<=5) and (D>=1 and D<=100) and (x2000>D and x2000<=200):
    x2001=r*x2000-D
    x2002=r*x2001-D
    x2003=r*x2002-D
    x2004=r*x2003-D
    x2005=r*x2004-D
    x2006=r*x2005-D
    x2007=r*x2006-D
    x2008=r*x2007-D
    x2009=r*x2008-D
    x2010=r*x2009-D
    print(x2001)
    print(x2002)
    print(x2003)
    print(x2004)
    print(x2005)
    print(x2006)
    print(x2007)
    print(x2008)
    print(x2009)
    print(x2010)
else:
    print("Error")