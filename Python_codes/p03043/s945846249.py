data=input().split()
N=int(data[0])
K=int(data[1])
ans=0
for i in range(1,N+1):
    dice=i
    n=0
    while 1<=dice<=K-1:
        dice*=2
        n+=1
    ans+=((1/2)**n)/N
print(ans)