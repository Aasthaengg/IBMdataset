N,K=map(int,input().split())
XY=[list(map(int,input().split())) for i in range(N)]
XY=sorted(XY,key=lambda x:x[0])
Mlst=[]

if N>=2:
    for s1 in range(N-1):
        for s2 in range(s1+1,N):
            x1,y1=XY[s1]
            x2,y2=XY[s2]
            y1,y2=min(y1,y2),max(y1,y2)
            count=2
            for i in range(s1+1,s2):
                count+=y1<=XY[i][1]<=y2
            if count>=K:
                Mlst.append((y2-y1)*(x2-x1))
if N>=3:
    for s1 in range(N-2):
        for s2 in range(s1+1,N-1):
            for s3 in range(s2+1,N):
                x1,y1=XY[s1]
                x2,y2=XY[s2]
                x3,y3=XY[s3]
                x1,x2=x1,x3
                y1,y2=min(y1,y2,y3),max(y1,y2,y3)
                count=2
                for i in range(s1+1,s3):
                    count+=y1<=XY[i][1]<=y2
                if count>=K:
                    Mlst.append((y2-y1)*(x2-x1))
if N>=4:
    for s1 in range(N-3):
        for s2 in range(s1+1,N-2):
            for s3 in range(s2+1,N-1):
                for s4 in range(s3+1,N):
                    x1,y1=XY[s1]
                    x2,y2=XY[s2]
                    x3,y3=XY[s3]
                    x4,y4=XY[s4]
                    x1,x2=x1,x4
                    y1,y2=min(y1,y2,y3,y4),max(y1,y2,y3,y4)
                    count=2
                    for i in range(s1+1,s4):
                        count+=y1<=XY[i][1]<=y2
                    if count>=K:
                        Mlst.append((y2-y1)*(x2-x1))
print(min(Mlst))
