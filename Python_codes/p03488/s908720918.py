s = input()
x,y = map(int,input().split())
 
X = []
Y = []
flag = 0
tmp = 0
for i in s:
    if i == "T":
        if flag == 0:
            if tmp != 0:
                X.append(tmp)
            flag = 1
            tmp = 0
        else:
            if tmp != 0:
                Y.append(tmp)
            flag = 0
            tmp = 0
    else:
        tmp += 1
if tmp != 0:
    if flag == 0:
        X.append(tmp)
    else:
        Y.append(tmp)

if s[0] !="T":
    tmpX = X[0]
    del X[0]
else:
    tmpX = 0

X = sorted(X)
Y = sorted(Y)
sumX = sum(X)
sumY = sum(Y)
tmpY = 0
 
ans = 0
 
if (x+sumX-tmpX)%2 == 1:
    ans = 1
else:
    mokuhyoX = (x+sumX-tmpX)//2
if (y+sumY-tmpY)%2 == 1:
    ans = 1
else:
    mokuhyoY = (y+sumY-tmpY)//2
if ans == 0:
	if mokuhyoX < 0 or mokuhyoY < 0:
	    ans = 1

# mokuhyoX
if ans == 0:
    dpX = [[False]*(mokuhyoX+1) for _ in range(len(X)+1)]
    dpX[0][0] = True
    for i in range(len(X)):
        for j in range(mokuhyoX+1):
            dpX[i+1][j] = dpX[i+1][j] or dpX[i][j]
            if j >= X[i]:
                dpX[i+1][j] = dpX[i+1][j] or dpX[i][j-X[i]]
    
    
# mokuhyoY
if ans == 0:
    dpY = [[False]*(mokuhyoY+1) for _ in range(len(Y)+1)]
    dpY[0][0] = True
    for i in range(len(Y)):
        for j in range(mokuhyoY+1):
            dpY[i+1][j] = dpY[i+1][j] or dpY[i][j]
            if j >= Y[i]:
                dpY[i+1][j] = dpY[i+1][j] or dpY[i][j-Y[i]]
 
if ans==0:
    if dpX[len(X)][mokuhyoX] == dpY[len(Y)][mokuhyoY] == True:
        ans = 0
    else:
        ans = 1
    
if ans == 1:
    print("No")
else:
    print("Yes")

