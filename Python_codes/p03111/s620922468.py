N,A,B,C=map(int,input().split())
l=[int(input()) for _ in range(N)]
dist=[A,B,C]
ans=float("inf")
for i in range(pow(4,N)):
    bit=[0]*N
    num=i
    x=[[],[],[]]
    cnt=0
    for j in range(N-1,-1,-1):
        bit[j]=num//pow(4,j)
        num=num%pow(4,j)
    #print(bit.count(1),bit.count(2),bit.count(3))
    if (bit.count(1)>0)and(bit.count(2)>0)and(bit.count(3)>0):
        #print(bit)
        for j in range(N):
            if bit[j]>0:
                x[bit[j]-1].append(l[j])
        for j in range(3):
            cnt=cnt+(len(x[j])-1)*10
            num=sum(x[j])
            cnt=cnt+abs(num-dist[j])
        ans=min(cnt,ans)
print(ans)
