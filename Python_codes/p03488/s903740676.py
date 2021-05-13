from collections import deque


s = input()

x,y = map(int,input().split())

xlis = []
ylis = []

slis = deque()
for i in s:
    slis.append(i)


while True:
    if len(slis) > 0 and slis[0] == "F":
        x -= 1
        slis.popleft()
    else:
        break

#print(slis,x)

direct = 0
tnum = 0
fnum = 0

while len(slis) > 0:

    nows = slis.popleft()

    if nows == "T":

        if tnum == 0 and fnum != 0:

            if  direct == 0:
                xlis.append(fnum)
            else:
                ylis.append(fnum)

            fnum = 0

        tnum += 1

    if nows == "F":

        direct = (direct + tnum) % 2
        tnum = 0
        fnum += 1

if fnum != 0:

    if direct == 0:
        xlis.append(fnum)
    else:
        ylis.append(fnum)




xdic = {}
ydic = {}


xdic[0] = 1
ydic[0] = 1


for i in xlis:

    nxdic = {}

    for j in xdic:
        nxdic[j + i] = 1
        nxdic[j - i] = 1

    xdic = nxdic.copy()

for i in ylis:

    nydic = {}

    for j in ydic:
        nydic[j + i] = 1
        nydic[j - i] = 1

    ydic = nydic.copy()

if x in xdic and y in ydic:
    print ("Yes")

else:
    print ("No")
