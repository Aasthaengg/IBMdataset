H,W = map(int,input().split())
s = [None]*H
for i in range(H):
    s[i] = input()

from collections import deque
def cango(x,y):
    cand =[]
    if x+1<=H-1:
        cand.append((x+1,y))
    if x-1>=0:
        cand.append((x-1,y))
    if y+1<=W-1:
        cand.append((x,y+1))
    if y-1>=0:
        cand.append((x,y-1))
    return cand
    
q = deque([(-1,-1,0,0,0)]) 
been = [[False]*W for _ in range(H)]

reach=False
while q:
    x_old,y_old,x_now,y_now,time = q.popleft()
    
    cand = cango(x_now,y_now)
    
    if x_now==H-1 and y_now==W-1:
        reach=True
        break
    
    for x_new,y_new in cand:
        if not been[x_new][y_new] and s[x_new][y_new]==".":
            q.append((x_now,y_now,x_new,y_new,time+1))
            been[x_new][y_new]=True
if reach:
    print( sum(ss.count(".") for ss in s)-time-1 )
else:
    print(-1)