N,C,K=map(int,input().split())
T=[int(input())for i in range(N)]
T.sort()
ans=0
bus_seat=0
tmp_time=0
for i in range(len(T)):
    if T[i]>tmp_time+K:
        bus_seat=0
    if bus_seat==0:
        ans+=1
        tmp_time=T[i]
    
    bus_seat+=1
    if bus_seat==C:
        bus_seat=0
print(ans)