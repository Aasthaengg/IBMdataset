import numpy as np
n=int(input())
x=[list(map(int, input().split())) for _ in range(n)]

now=0
nplace=[0,0]
noflag=False
for y in x:
    dis=sum(map(abs, (np.array(y[1:]) - np.array(nplace))))
    # print(dis)
    if not ((dis<=(y[0]-now)) & ((y[0]-now-dis)%2==0)):
        noflag=True

    now=y[0]
    nplace=y[1:]
print('Yes') if noflag==False else print('No')