n=int(input())

keta=len(str(n))

cnt=0

if keta%2==0:
    cnt+=9
    for i in range(4,keta+1,2):
        cnt+=9*(100**((i-2)//2))
        
if keta%2!=0:
    cnt+=9
    if keta==3:
        cnt+=n-99
    else:
        for i in range(5,keta+1,2):
            cnt+=9*(100**((i-3)//2))
            cnt+=n-(10**(i-1)-1)            

if keta==1:
    print(n)
else:
    print(cnt)