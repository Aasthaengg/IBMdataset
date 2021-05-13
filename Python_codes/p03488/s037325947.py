# -*- coding: utf-8 -*-
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = readline().decode().rstrip()
N = len(S)
x,y = map(int,readline().split())
t_cnt = 0
cnt_x1 = 0
cnt_x2 = 0
cnt_y = 0
X = []
Y = []
for i in range(N):
    if S[i] == 'F':
        if t_cnt == 0:
            cnt_x1 += 1
        else:
            if t_cnt % 2 == 0:
                cnt_x2 += 1
            else:
                cnt_y += 1
    else:
        t_cnt += 1
        if cnt_x2 != 0:
            X.append(cnt_x2)
            cnt_x2 = 0
        if cnt_y != 0:
            Y.append(cnt_y)
            cnt_y = 0
            
if cnt_x2 != 0:
    X.append(cnt_x2)
    cnt_x2 = 0
if cnt_y != 0:
    Y.append(cnt_y)
    cnt_y = 0

xN = len(X)
yN = len(Y)    
sumX = sum(X)
sumY = sum(Y)
x -= cnt_x1

if sumX - x < 0 or (sumX - x) % 2 != 0:
    print('No')
    sys.exit()
else:  
    xx = (sumX - x) // 2
if sumY - y < 0 or (sumY - y) % 2 != 0:
    print('No')
    sys.exit()
else:  
    yy = (sumY - y) // 2
    
dp_x = [0]*(xx+1) 
dp_x[0] = 1
for i in range(xN):
    w = X[i]
    for j in range(xx,w-1,-1):
        dp_x[j] = dp_x[j] or dp_x[j-w]
        
dp_y = [0]*(yy+1) 
dp_y[0] = 1
for i in range(yN):
    w = Y[i]
    for j in range(yy,w-1,-1):
        dp_y[j] = dp_y[j] or dp_y[j-w]

if dp_x[xx] and dp_y[yy]:
    print('Yes')
else:
    print('No')