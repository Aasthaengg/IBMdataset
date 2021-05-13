import numpy

x,n = map(int,input().split())
try:
    p = list(map(int,input().split()))
except EOFError:
    p =[]

a = numpy.abs(list(map(lambda z: z-x,p))).tolist()
if 0 not in a:
    print(x)
else:
    i = 1
    while i <= n:
        if a.count(i) == 2:
            i += 1
            continue
        elif a.count(i) == 1:
            if x+i not in p:
                print(x+i)
                break
        if x > 0:
            print(x-i)
        else:
            print(x+i)
        break