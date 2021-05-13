s=input()
x,y=map(int,input().split())
h=[]
v=[]
num=0
m=1
for i in s:
    if i=='F':
        num+=1
    else:
        if num!=0:
            if m==1:
                h.append(num)
            else:
                v.append(num)
        m=-m
        num=0
if num!=0:
    if m==1:
        h.append(num)
    else:
        v.append(num)
if s[0]=='F':
    x=x-h[0]
    del h[0]
sumh=sum(h)
nh=len(h)
dph=[]
if nh!=0:
    for i in range(nh+1):
        sub_list=[False]*(1+2*sumh)
        dph.append(sub_list)
    dph[0][sumh]=True
    for i in range(1,nh+1):
        for j in range(1+2*sumh):
            if j-h[i-1]>=0:
                dph[i][j]=dph[i][j] or dph[i-1][j-h[i-1]]
            if j+h[i-1]<=2*sumh:
                dph[i][j]=dph[i][j] or dph[i-1][j+h[i-1]]
    if 0<=x+sumh<=2*sumh:
        sh=dph[nh][x+sumh]
    else:
        sh=False
else:
    if x==0:
        sh=True
    else:
        sh=False
sumv=sum(v)
nv=len(v)
dpv=[]
if nv!=0:
    for i in range(nv+1):
        sub_list=[False]*(1+2*sumv)
        dpv.append(sub_list)
    dpv[0][sumv]=True
    for i in range(1,nv+1):
        for j in range(1+2*sumv):
            if j-v[i-1]>=0:
                dpv[i][j]=dpv[i][j] or dpv[i-1][j-v[i-1]]
            if j+v[i-1]<=2*sumv:
                dpv[i][j]=dpv[i][j] or dpv[i-1][j+v[i-1]]
    if 0<=y+sumv<=2*sumv:
        sv=dpv[nv][y+sumv]
    else:
        sv=False
else:
    if y==0:
        sv=True
    else:
        sv=False
if sh and sv:
    print('Yes')
else:
    print('No')
