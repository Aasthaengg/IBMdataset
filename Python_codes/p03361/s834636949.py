import numpy as np
h,w = list(map(int, input().split())) 
canvas = np.array([[np.nan]*w]*h).astype(int)

for i in range(h):
    s = input()
    for j in range(w):
        if( s[j] == '.'):
            canvas[i, j] = 0
        elif (s[j]=='#'):
            canvas[i, j] = 1

ret = True
for i in range(h):
    for j in range(w):
        if( canvas[i, j] == 1):

            check = False
            ch = i-1
            cw = j
            if( (0 <= ch & ch < h) & (0 <= cw & cw < w)):  
                if( canvas[ch,cw] == 1):
                    check = True
            ch = i
            cw = j-1
            if( (0 <= ch & ch < h) & (0 <= cw & cw < w)):  
                if( canvas[ch,cw] == 1):
                    check = True
            ch = i
            cw = j+1
            if( (0 <= ch & ch < h) & (0 <= cw & cw < w)):  
                if( canvas[ch,cw] == 1):
                    check = True
            ch = i+1
            cw = j
            if( (0 <= ch & ch < h) & (0 <= cw & cw < w)):  
                if( canvas[ch,cw] == 1):
                    check = True  
            if check == False:
                ret = False
                break
    if ret == False:
        break
if ret:
    print('Yes')
else:
    print('No')