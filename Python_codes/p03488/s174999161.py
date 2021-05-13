#082_D
s = input()
x, y = map(int, input().split())
xgo, ygo = [], []

cnt = 0
flg = True
check = True if s[0] == 'F' else False
for i in range(len(s)):
    if s[i] == 'T':
        if flg and cnt > 0:
            xgo.append(cnt)
        elif cnt > 0:
            ygo.append(cnt)
        cnt = 0
        flg = (flg + 1) % 2
    else:
        cnt += 1

if flg and cnt > 0:
    xgo.append(cnt)
elif cnt > 0:
    ygo.append(cnt)

flg1, flg2 = len(xgo)==0, len(ygo)==0

sum_x, sum_y = sum(xgo), sum(ygo)
dp1 = [[False for _ in range(2*sum_x+1)] for _ in range(len(xgo)+1)]
dp2 = [[False for _ in range(2*sum_y+1)] for _ in range(len(ygo)+1)]

if check:
    dp1[1][sum_x+xgo[0]] = True
    for i in range(2, len(xgo)+1):
        for j in range(-sum_x, sum_x+1):
            if 0 <= j+sum_x-xgo[i-1] <= 2*sum_x:
                if dp1[i-1][j+sum_x-xgo[i-1]]:
                    dp1[i][j+sum_x] = True
            if 0 <= j+sum_x+xgo[i-1] <= 2*sum_x:
                if dp1[i-1][j+sum_x+xgo[i-1]]:
                    dp1[i][j+sum_x] = True
else:
    dp1[0][sum_x] = True
    for i in range(1, len(xgo)+1):
        for j in range(-sum_x, sum_x+1):
            if 0 <= j+sum_x-xgo[i-1] <= 2*sum_x:
                if dp1[i-1][j+sum_x-xgo[i-1]]:
                    dp1[i][j+sum_x] = True
            if 0 <= j+sum_x+xgo[i-1] <= 2*sum_x:
                if dp1[i-1][j+sum_x+xgo[i-1]]:
                    dp1[i][j+sum_x] = True

dp2[0][sum_y] = True
for i in range(1, len(ygo)+1):
    for j in range(-sum_y, sum_y+1):
        if 0 <= j+sum_y-ygo[i-1] <= 2*sum_y:
            if dp2[i-1][j+sum_y-ygo[i-1]]:
                dp2[i][j+sum_y] = True
        if 0 <= j+sum_y+ygo[i-1] <= 2*sum_y:
            if dp2[i-1][j+sum_y+ygo[i-1]]:
                dp2[i][j+sum_y] = True
                
if flg1:
    flgx = (x == 0)
elif abs(x) > sum_x:
    flgx = False
else:
    flgx = dp1[len(xgo)][sum_x+x]
    
if flg2:
    flgy = (y == 0)
elif abs(y) >sum_y:
    flgy = False
else:
    flgy = dp2[len(ygo)][sum_y+y]
    
print('Yes' if flgx and flgy else 'No')