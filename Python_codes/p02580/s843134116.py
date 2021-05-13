h, w, m = map(int, input().split())
b = []
for i in range(m):
    hh, ww = map(int,input().split())
    hh -= 1
    ww -= 1
    b.append([hh, ww])
    
cnth = [0] * h
cntw = [0] * w
          
for i in range(m):
    hh, ww = b[i][0], b[i][1]
    cnth[hh] += 1
    cntw[ww] += 1
    
mh = max(cnth)
mw = max(cntw)

cnt_mh = 0
for i in range(h):
    if cnth[i] == mh:
        cnt_mh += 1
cnt_mw = 0
for i in range(w):
    if cntw[i] == mw:
        cnt_mw += 1

cnt_m = 0
for i in range(m):
    hh, ww = b[i][0], b[i][1]
    if cnth[hh] == mh and cntw[ww] == mw:
        cnt_m += 1
print(mh+mw) if cnt_mh*cnt_mw > cnt_m else print(mh+mw-1)
