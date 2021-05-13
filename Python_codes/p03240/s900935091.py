def dist(X,Y):
    return abs(X[0]-Y[0])+abs(X[1]-Y[1])
N = int(input())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[2],reverse=True)
for i in range(101):
    for j in range(101):
        flag=0
        x0,y0,h0 = A[0]
        H = h0+dist((i,j),(x0,y0))
        for k in range(1,N):
            x,y,h = A[k]
            if h>0 and H==h+dist((i,j),(x,y)):
                continue
            elif h>0 and H!=h+dist((i,j),(x,y)):
                flag=1
                break
            elif h==0 and H<=dist((i,j),(x,y)):
                continue
            elif h==0 and H>dist((i,j),(x,y)):
                flag = 1
                break
        if flag==0:
            Cx = i
            Cy = j
            break
    if flag==0:break
print(Cx,Cy,H)