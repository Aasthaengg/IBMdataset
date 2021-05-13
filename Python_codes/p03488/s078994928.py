
def main():
    s=input()
    x,y=map(int,input().split())

    lf = [0]
    tf = 0
    for i in range(len(s)):
        if s[i] =="F":
            lf[tf] += 1
        else:
            lf.append(0)
            tf += 1

    lx = [lf[i] for i in range(len(lf)) if i % 2 == 0]
    ly = [lf[i] for i in range(len(lf)) if i % 2 == 1]
    dpxcenter = sum(lx)
    if abs(x)>dpxcenter: return "No"
    dpxedge = dpxcenter*2+20
    dpx = [[False for _ in range(dpxedge)] for _ in range(len(lx)+1)]
    dpx[1][dpxcenter+lx[0]+10] = True
    for i in range(1,len(lx)):
        for j in range(dpxedge):
            if j-lx[i] >= 0:
                dpx[i+1][j] = dpx[i][j-lx[i]]
            if j+lx[i] < dpxedge:
                dpx[i+1][j] = dpx[i+1][j] or dpx[i][j+lx[i]]

    dpycenter = sum(ly)
    if abs(y)>dpycenter: return "No"
    dpyedge = dpycenter*2+20
    dpy = [[False for _ in range(dpyedge)] for _ in range(len(ly)+1)]
    dpy[0][dpycenter+10] = True
    for i in range(len(ly)):
        for j in range(dpyedge):
            if j-ly[i] >= 0:
                dpy[i+1][j] = dpy[i][j-ly[i]]
            if j+ly[i] < dpyedge:
                dpy[i+1][j] = dpy[i+1][j] or dpy[i][j+ly[i]]

    if dpx[-1][x+dpxcenter+10] and dpy[-1][y+dpycenter+10]:return "Yes"
    else:return "No"

print(main())