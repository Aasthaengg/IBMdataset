abalable_H = []
N = int(input())
x = []
y = []
h = []
first =-1
for i in range(0,N,1):
    tmpx,tmpy,tmph = map(int,input().split())
    x.append(tmpx)
    y.append(tmpy)
    h.append(tmph)
    if tmph !=0 and first == -1:
        first = i

for cx in range(0,101,1):
    for cy in range(0,101,1):
        H = h[first]+abs(x[first]-cx)+abs(y[first]-cy)
        ok = True
        for i in range(0,N,1):
            if h[i] != max(H-abs(cx-x[i])-abs(cy-y[i]),0):
                ok =False
        if ok == True:
            print(cx,cy,H)
            break