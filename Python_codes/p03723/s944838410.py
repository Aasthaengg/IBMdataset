import numpy as np
lis=np.array(list(map(int,input().split())))
cnt=0
for i in range(1000000):
    if lis[0]%2==0 and lis[1]%2==0 and lis[2]%2==0:
        if lis[0]==lis[1]==lis[2]:
            print('-1')
            break
        else:   
            lis=lis/2
            a=lis[1]+lis[2]
            b=lis[0]+lis[2]
            c=lis[0]+lis[1]
            lis[0]=a
            lis[1]=b
            lis[2]=c
            cnt+=1
    else:
        print(cnt)
        break