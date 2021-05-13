import numpy as np
N = int(input().strip('\n'))
k2 = 1+np.sqrt(1+8*N)
if k2%2==0:
    k=int(k2/2)
    print('Yes')
    print(k)
    yel = [1]
    red = [1]
    for i in range(1,k-1):
        yel.append(yel[i-1]+1+i)
        red.append(red[i-1]+i)
    yel = np.array(yel).astype('int32')
    red = np.array(red).astype('int32')
    print(k-1,*yel)
    print(k-1,*red)
    for i in range(1,k-1):
        fs = np.arange(red[i],red[i]+i).astype('int32')
        sc = red[i:]+i
        fs = np.concatenate((fs,sc))
        print(k-1,*fs)
else:
    print('No')