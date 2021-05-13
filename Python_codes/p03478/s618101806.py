n,a,b = map(int,input().split())
c = 0
for i in range(1,n+1):
    if i < 10:
        x = str(i)
        xsum = int(x[0])
        if xsum >= a and xsum <= b:
            c += i
    elif i < 100:
        x = str(i)
        xsum = int(x[0]) + int(x[1])
        if xsum >= a and xsum <= b:
            c += i
    elif i < 1000:
        x = str(i)
        xsum = int(x[0]) + int(x[1]) + int(x[2])
        if xsum >= a and xsum <= b:
            c += i
    elif i < 10000:
        x = str(i)
        xsum = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3])
        if xsum >= a and xsum <= b:
            c += i
    else:
        x = str(i)
        xsum = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3]) + int(x[4])
        if xsum >= a and xsum <= b:
            c += i
print(c)