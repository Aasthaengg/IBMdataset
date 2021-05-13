N,C,K=map(int,input().split())
T=[0]*N
for i in range(N):
    T[i]=int(input())

T=sorted(T)

las=T[0]+K
ans,cnt=0,0

for t in T:
    if cnt<C and las>=t:
        cnt+=1
    else:
        ans+=1
        cnt=1
        las=t+K

if cnt>0:
    ans+=1
    
print(ans)