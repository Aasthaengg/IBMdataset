s = list(input())
x,y = map(int,input().split())
i = 0
while i < len(s) and s[i] == "F":
    i += 1
    x -= 1

l = []
r = []
check = 1
count = 0
while i < len(s):
    if s[i] == "T":
        if count >0:
            if check == 1:
                l.append(count)
            else:
                r.append(count)
        check *= -1
        count = 0
    else:
        count += 1
    i += 1

if count >0:
    if check == 1:
        l.append(count)
    else:
        r.append(count)       

    
if abs(x) > sum(l) or abs(y) > sum(r):
    print("No")
    exit() 

dpx = [[0]*(sum(l)*2+3) for i in range(len(l)+1)]
lx = sum(l)*2+3
dpx[0][sum(l)] = 1
for i in range(len(l)):
    for j in range(lx):
        if dpx[i][j] == 1:
            dpx[i+1][j+l[i]] = 1
            dpx[i+1][j-l[i]] = 1

dpy = [[0]*(sum(r)*2+3) for i in range(len(r)+1)]
rx = sum(r)*2+3
dpy[0][sum(r)] = 1
for i in range(len(r)):
    for j in range(rx):
        if dpy[i][j] == 1:
            dpy[i+1][j+r[i]] = 1
            dpy[i+1][j-r[i]] = 1
if dpx[-1][sum(l)+x] == 1 and dpy[-1][sum(r)+y] == 1:
    print("Yes")
else:
    print("No")