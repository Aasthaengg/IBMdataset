N,M=map(int,input().split())
ab=[]
for i in range(N):
    ab.append(list(map(int,input().split())))
cd=[]
for i in range(M):
    cd.append(list(map(int,input().split())))
def Mandis(x1,x2,y1,y2):
    e=abs(x1-x2)+abs(y1-y2)
    return e
for i in range(N):
    g=0
    for j in range(M-1):
        if Mandis(ab[i][0],cd[j+1][0],ab[i][1],cd[j+1][1])<Mandis(ab[i][0],cd[g][0],ab[i][1],cd[g][1]):
            g=j+1
    print(g+1)