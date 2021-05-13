n,y=map(int,input().split())
flag=0
for i in range(n+1):
    for j in range(n+1):
        z=n-i-j
        if z<0:
            continue
        if int(i*10000+j*5000+z*1000)==y:
            flag=1
            break
    if flag==1:
        break
if flag==1:
    print(str(i)+' '+str(j)+' '+str(z))
else:
    print('-1 -1 -1')