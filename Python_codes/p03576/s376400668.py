N,K=map(int,input().split())
v=[]
for i in range(0,N):
    x,y=map(int,input().split())
    v.append([x,y])

v.sort()

ans=10**20
for i in range(0,N-1):
    for j in range(i+1,N):
        data=[]
        for k in range(i,j+1):
            x,y=v[k]
            data.append(y)
        data.sort()
        if K>len(data):
            continue
        else:
            for k in range(0,len(data)-K+1):
                w=v[j][0]-v[i][0]
                h=data[k+K-1]-data[k]
                test=w*h
                if ans>test:
                    ans=test

print(ans)