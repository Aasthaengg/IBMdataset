s = list(str(input()))
x,y = map(int,input().split())

i = 0
while i < len(s) and s[i] =="F":
    i += 1
x -= i
s = s[i:]

m = [[],[]]
num = 0

for i in range(len(s)):
    if s[i] == "F":
        m[num][-1] += 1
    else:
        num += 1
        num %= 2
        m[num].append(0)

#print("m",m)

sumx = sum(m[0])

dpx = [False]*(2*sumx+3) #index(sumx+1)が座標0
dpx[sumx+1] = True
#print("dpx",dpx)

for p in m[0]:
    dpx_pre = dpx[:]
    dpx = [False]*(2*sumx+3)
    for i in range(2*sumx+3):
        if i-p >= 0:
            dpx[i-p] = dpx_pre[i] or dpx[i-p]
            #print("dpx",dpx)
        if i+p < 2*sumx+3:
            dpx[i+p] = dpx_pre[i] or dpx[i+p]
            #print("dpx",dpx)
    #print("dpx",dpx)

sumy = sum(m[1])
dpy = [False]*(2*sumy+3) #index(sumy+1)が座標0
dpy[sumy+1] = True
#print("dpy",dpy)

for p in m[1]:
    dpy_pre = dpy[:]
    dpy = [False]*(2*sumy+3)
    for i in range(2*sumy+3):
        if i-p >= 0:
            dpy[i-p] = dpy_pre[i] or dpy[i-p]
        if i+p < 2*sumy+3:
            dpy[i+p] = dpy_pre[i] or dpy[i+p]
    #print("dpy",dpy)

if abs(x) > sumx+1 or abs(y) > sumy+1:
    print("No")
elif dpx[x+(sumx+1)] and dpy[y+(sumy+1)]:
    print("Yes")
else:
    print("No")