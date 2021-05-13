import numpy as np
s = input()
x, y = map(int, input().split())

i = 0
stock = 0
sl = []
while i < len(s):
    if s[i] == 'F':
        stock+=1
        i+=1
    else:
        sl.append(stock)
        stock = 0
        i+=1
else:
    sl.append(stock)

x-=sl[0]
ymove = sl[1::2]
xmove = sl[2::2]

dpx = np.zeros(16002).astype(int)
dpx[8000] = 1
for i in range(len(xmove)):
    idx = np.where(dpx==1)[0]
    ndpx = np.zeros(16002)
    ndpx[idx+xmove[i]] = True
    ndpx[idx-xmove[i]] = True
    dpx = ndpx

dpy= np.zeros(16002).astype(int)
dpy[8000] = 1
for i in range(len(ymove)):
    idx = np.where(dpy==1)[0]
    ndpy = np.zeros(16002)
    ndpy[idx+ymove[i]] = True
    ndpy[idx-ymove[i]] = True
    dpy = ndpy

if dpx[x+8000] == 1 and dpy[y+8000] == 1:
    print('Yes')
else:
    print('No')

