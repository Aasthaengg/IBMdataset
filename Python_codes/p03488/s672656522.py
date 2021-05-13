S = input()
X,Y = map(int,input().split())
T0 = 0
XList = []
YList = []
N = len(S)
t = 0
f = 0
for i in range(N):
    c = S[i]
    if c == 'F':
        f += 1
    else:
        if t == 0:
            T0 = f
        else:
            if t % 2 == 0:
                if f > 0:
                    XList.append(f)
            else:
                if f > 0:
                    YList.append(f)
        f = 0
        t += 1
if f > 0:
    if t == 0:
        T0 = f
    else:
        if t % 2 == 0:
            XList.append(f)
        else:
            YList.append(f)

xset = set()
yset = set()
tset = set()

xset.add( T0 )
for f in XList:
    tset.clear()
    for x in xset:
        tset.add(x+f)
        tset.add(x-f)
    xset.clear()
    for x in tset:
        xset.add(x)

yset.add( 0 )
for f in YList:
    tset.clear()
    for y in yset:
        tset.add(y+f)
        tset.add(y-f)
    yset.clear()
    for y in tset:
        yset.add(y)

if X in xset and Y in yset:
    print('Yes')
else:
    print('No')
