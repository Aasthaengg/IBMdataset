import numpy as np


h,w,k = map(int,input().split())
connect = [[0 for i in range(w)] for j in range(w)]

if w == 1:
    print(1)
else:
    allstate = [""]
    befstate = [""]
    for i in range(w-1):
        for s in befstate:
            if s == "":
                allstate.append(s+str(i))
            else:
                last = int(s[-1])
                if (i-last)!=1:
                    allstate.append(s+str(i))
        befstate = allstate.copy()
        # print(befstate)
    # print(allstate)
    tot = len(allstate)
    for s in allstate:
        for c in s:
            temp = int(c)
            connect[temp][temp+1] += 1
            connect[temp+1][temp] += 1
    for i in range(w):
        temp = sum(connect[i])
        connect[i][i] = tot-temp
    buf = [0 for i in range(w)]
    buf[0] = 1
    for i in range(h):
        nbuf = [0 for i in range(w)]
        for j in range(w):
            for l in range(w):
                nbuf[l] += buf[j]*connect[j][l]
                nbuf[l]%=10**9+7
        buf = nbuf.copy()
    # print(buf)
    print(buf[k-1])

