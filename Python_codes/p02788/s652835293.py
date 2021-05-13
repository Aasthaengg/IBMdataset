N,D,A=map(int,input().split())
monster=[]
for i in range(0,N):
    x,h=map(int,input().split())
    monster.append([x,h])

monster.sort()

H=[monster[i][1] for i in range(0,N)]

right_2d=[0 for i in range(0,N)]
for i in range(0,N):
    start=i
    end=N-1
    while end-start>1:
        test=(end+start)//2
        if 2*D+monster[i][0]>=monster[test][0]:
            start=test
        else:
            end=test
    if 2*D+monster[i][0]>=monster[end][0]:
        right_2d[i]=end
    else:
        right_2d[i]=start

imos=[0 for i in range(0,N+1)]
ans=0
for i in range(0,N):
    H[i]-=imos[i]
    if H[i]>0:
        count=(H[i]+A-1)//A
        ans+=count
        imos[i]+=A*count
        imos[right_2d[i]+1]-=A*count

    imos[i+1]+=imos[i]

print(ans)