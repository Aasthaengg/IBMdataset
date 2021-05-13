N,K=map(int, input().split())
V=list(map(int, input().split()))

#とるか戻すか
ruil=[0]*N
ruil[0]=V[0]

ruir=[0]*N
ruir[0]=V[-1]
for i in range(1,N):
    ruil[i]=ruil[i-1]+V[i]
    ruir[-(i+1)]=ruir[-i]+V[-(i+1)]
#操作何回やるか 0~K
#K回のうちX回とる　K-X回戻す 0~K
#左右の割合　0~X
ans=0
for i in range(K+1):
    if i==0:
        continue
    for j in range(0,i+1):
        if i/2<=j:
            continue
        #j: 戻す回数
        #i-j取る回数
        for k in range(i-j+1):
            if i-j>=N:
                get=V
            else:
                if i-j-k==0:
                    get=V[:k]
                else:
                    get=V[:k]+V[-(i-j-k):]
            get=sorted(get)
            #print(get,i)
            score=sum(get)-sum(get[:j])
            ans=max(ans, score)
            #print(score, get,i-j,j,k)

print(ans)

