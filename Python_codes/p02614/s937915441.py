import numpy as np
hwk=input().split()
H=int(hwk[0])
W=int(hwk[1])
K=int(hwk[2])
bits=np.zeros(H+1,dtype='int64')
c = [input() for _ in range(H)]
ans=int(0)
while bits[H]==0:
    dp=np.zeros(H*W+1,dtype='int64')
    dp[0]+=1
    for j in range(W):
        kaz=0
        for i in range(H):
            if bits[i]==1 and c[i][j]=='#':
                kaz+=1
        for i in range(H*W,kaz-1,-1):
            dp[i]+=dp[i-kaz]
    ans+=dp[K]

    bits[0]+=1
    bas=0
    while bits[bas]==2:
        bits[bas]=0
        bas+=1
        bits[bas]+=1
print(ans)





