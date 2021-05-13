n,W=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
w1=l[0][0]
l.sort(key=lambda x : x[1]*-1)
l0,l1,l2,l3 = [],[],[],[]
for w,v in l:
    if w==w1:
        l0.append(v)
    if w==w1+1:
        l1.append(v)
    if w==w1+2:
        l2.append(v)
    if w==w1+3:
        l3.append(v)
sl1,sl2,sl3,sl0=[0],[0],[0],[0]
tl=0
for i in range(len(l0)):
    tl += l0[i]
    sl0.append(tl)
tl=0
for i in range(len(l1)):
    tl += l1[i]
    sl1.append(tl)
tl=0
for i in range(len(l2)):
    tl += l2[i]
    sl2.append(tl)
tl=0
for i in range(len(l3)):
    tl += l3[i]
    sl3.append(tl)
res = 0
for a in range(len(sl0)):
    for b in range(len(sl1)):
        for c in range(len(sl2)):
            for d in range(len(sl3)):
                if w1*a+(w1+1)*b+(w1+2)*c+(w1+3)*d <= W:
                    res = max(res,sl0[a]+sl1[b]+sl2[c]+sl3[d])
print(res)