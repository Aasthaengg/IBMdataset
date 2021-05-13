import sys

n=int(input())
P=[]
for i in range(n):
    x,y,h=map(int,input().split())
    P.append([h,x,y])
P=list(reversed(sorted(P)))

for x in range(101):
    for y in range(101):
        flag=0
        H=P[0][0]+abs(P[0][1]-x)+abs(P[0][2]-y)
        for p in P:
            ph=p[0]
            px=p[1]
            py=p[2]
            if ph==0:
                if H-abs(px-x)-abs(py-y)>0:
                    flag=1
                    break
            else:
                if H-abs(px-x)-abs(py-y)!=ph:
                    flag=1
                    break
        if flag==1:
            continue
        else:
            print(x,y,H)
            sys.exit()