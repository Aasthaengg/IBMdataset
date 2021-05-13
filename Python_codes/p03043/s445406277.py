N,K=map(int,input().split())

ans=0

baisuu=1
multiplier=0
count=[0]
for i in range(N,0,-1):
    while baisuu*i<K:
        baisuu*=2
        multiplier+=1
        count.append(0)
    
    count[multiplier]+=1

ans=0
for i in range(len(count)):
    ans+=count[i]*0.5**i

ans/=N
print(ans)