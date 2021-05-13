N,M=map(int,input().split())
AC=[0]*N
WA=[0]*N
pts=0
pena=0
for i in range(M):
    a,b=map(str,input().split())
    if b=='AC':
        if AC[int(a)-1]==0:
            AC[int(a)-1]=1
            pts+=1
            pena+=WA[int(a)-1]
    else:
        WA[int(a)-1]+=1
print(pts,pena)