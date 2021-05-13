import sys

n=int(input())
xyh=[[] for i in range(n)]
for i in range(n):
    x,y,h=map(int,input().split())
    xyh[i].append(x)
    xyh[i].append(y)
    xyh[i].append(h)
for i in range(101):
    for j in range(101):
        f=0
        dis=[[i] for i in range(205)]
        for q in range(n):
            x=xyh[q][0]
            y=xyh[q][1]
            h=xyh[q][2]
            d=abs(x-i)+abs(y-j)
            
            if len(dis[d])==1:
                dis[d].append(h)
            elif len(dis[d])!=1 and dis[d][1]!=h:
                f=1
        
        dis=[dis[e] for e in range(205) if len(dis[e])!=1]
        m=len(dis)
        if m==1 and f==0:
            print(i,j,dis[0][0]+dis[0][1])
            sys.exit()
            
        else:
            if all(dis[e][0]+dis[e][1]==dis[e+1][0]+dis[e+1][1] for e in range(m-1) if dis[e+1][1]!=0) and f==0:
                print(i,j,dis[0][0]+dis[0][1])
                sys.exit()

