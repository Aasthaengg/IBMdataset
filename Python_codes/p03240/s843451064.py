from copy import copy
N=int(input())
K=100

Data=[]
for i in range(N):
    x,y,h=map(int,input().split())
    Data.append((x,y,h))

Data.sort(key=lambda x:-x[-1])
for i in range(N):
    x,y,h=Data[i]

    if i==0:
        C=[]
        for X in range(K+1):
            for Y in range(K+1):
                H=h+abs(x-X)+abs(y-Y)
                if H>0:
                    C.append((X,Y,H))
    else:
        D=[]
        for (X,Y,H) in C:
            if max(H-abs(x-X)-abs(y-Y),0)==h:
                D.append((X,Y,H))
        C=copy(D)

X,Y,H=C[0]
print(X,Y,H)