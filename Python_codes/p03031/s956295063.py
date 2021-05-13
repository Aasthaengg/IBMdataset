import numpy as np

N,M=map(int,input().split())
ks=np.array([[int(i) for i in input().split()] for _ in range(M)])
p=list(map(int,input().split()))

ans=0

for i in range(2**N):

    # swにスイッチのオンオフを記録
    sw=[0]*N
    for j in range(N):
        if (i>>j)&1:
            sw[j]=1

    count=0
    for denkyu_no in range(M):
        if sum([sw[ks[denkyu_no][j+1]-1] for j in range(ks[denkyu_no][0])])%2 ==p[denkyu_no]:
            count +=1

    if count==M:
        ans+=1
print(ans)