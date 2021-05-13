N = int(input())
i=abs(N)
lis = [0 for i in range(150)]
ind= 0
if i>0:
    while i>0:
        am = i%4
        i = i//4
        if N>0:
            lis[ind]=am
            lis[ind+1]=0
        else:
            lis[ind]=am
            lis[ind+1]=am
        ind+=2

ind=0
for i in range(148):
    #print(lis)
    if lis[i]==2:
        lis[i]=0
        lis[i+1]+=1
        lis[i+2]+=1
    elif lis[i]==3:
        lis[i]=1
        lis[i+1]+=1
        lis[i+2]+=1
    elif lis[i]>=4:
        lis[i+2]+=lis[i]//4
        lis[i]%=4

lis.reverse()
if N!=0:
    fir = lis[50:].index(1)
    map = map(str,lis[fir:])
    tmp = ''.join(map)
    print(int(tmp))
else:
    print(0)
