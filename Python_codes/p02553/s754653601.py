a,b,c,d = map(int,input().split())
def getmax(a,b):
    if a>b:
        return a
    else:
        return b
def getmin(a,b):
    if a<b:
        return a
    else:
        return b
if (a>0 and b>0 and c<0 and d<0) or (a<0 and b<0 and c>0 and d>0):
    x = getmin(a,b)
    y = getmax(c,d)
    max = x*y
    x = getmax(a,b)
    y = getmin(c,d)
    min = x*y
    if max > min:
        print(max)
    else:
        print(min)
else:
    x = getmax(a,b)
    y = getmax(c,d)
    max = x*y
    x = getmin(a,b)
    y = getmin(c,d)
    min = x*y
    if max > min:
        print(max)
    else:
        print(min)
