W,H,N = map(int, input().split())
w=[0]*W
h=[0]*H
for i in range(N):
    x,y,a = map(int, input().split())
    if a==1:
        for i in range(x):
            w[i]=1
    if a==2:
        for i in range(x,W):
            w[i]=1
    if a==3:
        for i in range(y):
            h[i]=1
    if a==4:
        for i in range(y,H):
            h[i]=1
 
print(w.count(0)*h.count(0))