W,H,N = map(int,input().split())
a1 = []
a2 = []
a3 = []
a4 = []
for i in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        a1.append(x)
    elif a == 2:
        a2.append(x)
    elif a == 3:
        a3.append(y)
    else:
        a4.append(y)
a1.sort(reverse=True)
a2.sort()
a3.sort(reverse=True)
a4.sort()
if a1:
    l = a1[0]
else:
    l = 0
if a2:
    r = a2[0]
else:
    r = W
if a3:
    d = a3[0]
else:
    d = 0
if a4:
    u = a4[0]
else:
    u = H
if r >= l and u >= d:
    print((r-l)*(u-d))
else:
    print(0)