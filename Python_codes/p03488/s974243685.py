import sys
s = input()
gx,gy = map(int, input().split(' '))
x_d = [0]
y_d = []
cnt = 0
for i in range(len(s)):
    if s[i] == "T":
        cnt += 1
        if cnt % 2 == 0:
            x_d.append(0)
        elif cnt % 2 == 1:
            y_d.append(0)
    if s[i] == "F":
        if cnt % 2 == 0:
            x_d[-1] += 1
        elif cnt % 2 == 1:
            y_d[-1] += 1
gx -= x_d[0]
x_d[0] = 0
x_d.append(0)
y_d.append(0)
if (sum(x_d)-gx) % 2 or (sum(y_d)-gy) % 2 or sum(x_d) < abs(gx) or sum(y_d) < abs(gy):
    print("No")
    sys.exit()
x_n = (sum(x_d)-gx)//2
y_n = (sum(y_d)-gy)//2
DPx = [[False for i in range(x_n+2)] for j in range(len(x_d))]
DPy = [[False for i in range(y_n+2)] for j in range(len(y_d))]
for x in DPx:
    x[0] = True
for y in DPy:
    y[0] = True
for i in range(len(x_d)-1):
    for j in range(x_n+1):
        if DPx[i][j]:
            DPx[i+1][j] = True
            if j+x_d[i] <= x_n+1:
                DPx[i+1][j+x_d[i]] = True
for i in range(len(y_d)-1):
    for j in range(y_n+1):
        if DPy[i][j]:
            DPy[i+1][j] = True
            if j+y_d[i] <= y_n+1:
                DPy[i+1][j+y_d[i]] = True
if DPx[len(x_d)-1][x_n] and DPy[len(y_d)-1][y_n]:
    print("Yes")
else:
    print("No")