H,W,M=map(int,input().split())
bomb=[]
h=[0]*H
w=[0]*W
for i in range(M):
    hi,wi=map(int,input().split())
    h[hi-1] += 1
    w[wi-1] += 1
    bomb.append([hi,wi])    
maxh = max(h)
maxw = max(w)
ans = maxh +  maxw
lh=[]
lw=[]
for i in range(len(h)):
    if h[i] == maxh:
        lh.append(i+1)
for i in range(len(w)):
    if w[i] == maxw:
        lw.append(i+1)
a = 0
for i in range(M):
    if ans == h[bomb[i][0]-1]+w[bomb[i][1]-1]:
        a += 1
if a == len(lh)*len(lw):
    print(ans-1)
else:
    print(ans)