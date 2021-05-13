N=int(input())
L=[]
for h in range(N):
    Cx,Cy,h=map(int,input().split())
    L.append([h,Cx,Cy])
L.sort(reverse=True)

for x in range(101):
    for y in range(101):
        cond=True
        H=L[0][0]+abs(x-L[0][1])+abs(y-L[0][2])
        for i in range(1,N):
            h=L[i][0]+abs(x-L[i][1])+abs(y-L[i][2])
            if L[i][0]>0:
                if h!=H:
                    cond=False
                    break
            else:
                if h<H:
                    cond=False
                    break
        if cond:
            break
    if cond:
        break

print(x,y,H)
