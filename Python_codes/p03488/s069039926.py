s = input().strip()
x,y = map(int,input().split())
AX = []
AY = []
flag = 0
cnt = 0
for i in range(len(s)):
    if s[i]=="F":
        cnt += 1
    else:
        if flag==0:
            if cnt>0:
                AX.append(cnt)
                cnt = 0
            flag = 1
        else:
            if cnt>0:
                AY.append(cnt)
                cnt = 0
            flag = 0
if cnt>0 and flag==0:
    AX.append(cnt)
if cnt>0 and flag==1:
    AY.append(cnt)
Nx = sum(AX)
dpX = [[0 for _ in range(2*Nx+1)] for _ in range(len(AX)+1)]
dpX[0][Nx] = 1
if s[0]=="F":
    dpX[1][Nx+AX[0]] = 1
    for i in range(1,len(AX)):
        for j in range(2*Nx+1):
            if j+AX[i]<=2*Nx:
                dpX[i+1][j+AX[i]] = dpX[i+1][j+AX[i]] or dpX[i][j]
            if 0<=j-AX[i]:
                dpX[i+1][j-AX[i]] = dpX[i+1][j-AX[i]] or dpX[i][j]
else:
    for i in range(len(AX)):
        for j in range(2*Nx+1):
            if j+AX[i]<=2*Nx:
                dpX[i+1][j+AX[i]] = dpX[i+1][j+AX[i]] or dpX[i][j]
            if 0<=j-AX[i]:
                dpX[i+1][j-AX[i]] = dpX[i+1][j-AX[i]] or dpX[i][j]
Ny = sum(AY)
dpY = [[0 for _ in range(2*Ny+1)] for _ in range(len(AY)+1)]
dpY[0][Ny] = 1
for i in range(len(AY)):
    for j in range(2*Ny+1):
        if j+AY[i]<=2*Ny:
            dpY[i+1][j+AY[i]] = dpY[i+1][j+AY[i]] or dpY[i][j]
        if 0<=j-AY[i]:
            dpY[i+1][j-AY[i]] = dpY[i+1][j-AY[i]] or dpY[i][j]
if Nx==0 and x!=0 or Ny==0 and y!=0:
    print("No")
elif abs(x)>Nx or abs(y)>Ny:
    print("No")
elif dpX[len(AX)][Nx+x]==1 and dpY[len(AY)][Ny+y]==1:
    print("Yes")
else:
    print("No")