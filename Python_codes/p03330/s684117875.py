N,C=map(int,input().split())
D=[[]for i in range(C)]
for i in range(C):
    D[i]=list(map(int,input().split()))
c=[[] for i in range(N)]
for i in range(N):
    c[i]=list(map(int,input().split()))
data0=[0 for i in range(0,C+1)]
data1=[0 for i in range(0,C+1)]
data2=[0 for i in range(0,C+1)]

for i in range(0,N):
    for j in range(0,N):
        if (i+j)%3==0:
            data0[c[i][j]]+=1
        elif (i+j)%3==1:
            data1[c[i][j]]+=1
        else:
            data2[c[i][j]]+=1

ans=10**100
for i in range(1,C+1):
    for j in range(1,C+1):
        for k in range(1,C+1):
            if i!=j and j!=k and k!=i:
                test=sum(data0[l]*D[l-1][i-1] for l in range(1,C+1))+sum(data1[l]*D[l-1][j-1] for l in range(1,C+1))+sum(data2[l]*D[l-1][k-1] for l in range(1,C+1))
                if test<ans:
                    ans=test
print(ans)