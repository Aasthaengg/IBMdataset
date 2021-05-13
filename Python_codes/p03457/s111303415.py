N=int(input())
P=[(0,0,0)]*(N+1)

D=[0]*(N+1)

P[0]=(0,0,0)
D[0]=1
for i in range(1,N+1):
    t,x,y=map(int,input().split())
    dt=t-P[i-1][0]
    dx=abs(x-P[i-1][1])
    dy=abs(y-P[i-1][2])
    if dt < (dx+dy): #時間<移動距離
        print('No')
        break
    if ((dx+dy)==0 and dt%2!=0): #移動しない場合には時間はmod2==0
        print('No')
        break
    #if (dt-(dx+dy))%2==0 or dt%(dx+dy)==0:
    if (dt-(dx+dy))%2!=0:
        print('No')
        break
    
    P[i]=(t,x,y)
else:
    print('Yes')    