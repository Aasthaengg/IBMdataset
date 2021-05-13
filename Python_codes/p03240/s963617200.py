N=int(input())
x=[]
y=[]
h=[]
for _ in range(N):
    a,b,c=map(int,input().split())
    x.append(a)
    y.append(b)
    h.append(c)
k=0
for i in range(N):
    if h[i]!=0:
        k=i
        break
for cx in range(101):
    for cy in range(101):
        H=h[k]+abs(x[k]-cx)+abs(y[k]-cy)
        for i in range(N):
            if max(H-abs(x[i]-cx)-abs(y[i]-cy),0)!=h[i]:
                break
        else:
            print(cx,cy,H)
            break
    else:
        continue
    break
