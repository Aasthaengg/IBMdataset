s = input().strip()
x,y = map(int,input().split())
C = {}
cur = 0
cnt = 0
for i in range(len(s)):
    if s[i]=="F":
        cnt += 1
    else:
        C[cur] = cnt
        cur += 1
        cnt = 0
C[cur] = cnt
AX = []
AY = []
for a in C:
    if a>0 and a%2==0 and C[a]>0:
        AX.append(C[a])
    elif a%2==1 and C[a]>0:
        AY.append(C[a])
cntx = sum(AX)
dpx = [[0 for _ in range(2*cntx+1)] for _ in range(len(AX)+1)]
dpx[0][cntx] = 1
if cntx>0:
    dpx[1][cntx-AX[0]] = 1
    dpx[1][cntx+AX[0]] = 1
    for i in range(2,len(AX)+1):
        for j in range(-cntx,cntx+1):
            if -cntx<=j-AX[i-1]:
                dpx[i][j+cntx] = dpx[i-1][j-AX[i-1]+cntx]
                if j+AX[i-1]<=cntx:
                    dpx[i][j+cntx] = max(dpx[i][j+cntx],dpx[i-1][j+AX[i-1]+cntx])
            elif j+AX[i-1]<=cntx:
                dpx[i][j+cntx] = dpx[i-1][j+AX[i-1]+cntx]
cnty = sum(AY)
dpy = [[0 for _ in range(2*cnty+1)] for _ in range(len(AY)+1)]
dpy[0][cnty] = 1
if cnty>0:
    dpy[1][cnty-AY[0]] = 1
    dpy[1][cnty+AY[0]] = 1
    for i in range(2,len(AY)+1):
        for j in range(-cnty,cnty+1):
            if -cnty<=j-AY[i-1]:
                dpy[i][j+cnty] = dpy[i-1][j-AY[i-1]+cnty]
                if j+AY[i-1]<=cnty:
                    dpy[i][j+cnty] = max(dpy[i][j+cnty],dpy[i-1][j+AY[i-1]+cnty])
            elif j+AY[i-1]<=cnty:
                dpy[i][j+cnty] = dpy[i-1][j+AY[i-1]+cnty]
if C[0]-cntx<=x<=C[0]+cntx and dpx[len(AX)][x-C[0]+cntx]==1 and -cnty<=y<=cnty and dpy[len(AY)][y+cnty]==1:
    print("Yes")
else:
    print("No")