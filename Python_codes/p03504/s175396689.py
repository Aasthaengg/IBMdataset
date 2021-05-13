n,C=map(int,input().split())
stc=[list(map(int,input().split())) for i in range(n)]
d=[[0]*(10**5+1) for i in range(C+1)]
for u in stc:
    s,t,c=u
    if d[c][s]==-1:
        d[c][s]=0
        if d[c][t]==1:
            d[c][t]=0
        else:
            d[c][t]=-1
    else:
        d[c][s]=1
        if d[c][t]==1:
            d[c][t]=0
        else:
            d[c][t]=-1
for i in range(1,C+1):
    for j in range(10**5):
        if d[i][j+1]==1:
            d[i][j]+=1
            d[i][j+1]=0
data=[0]*(10**5+1)
for j in range(1,C+1):
    data[0]+=d[j][0]
for i in range(1,10**5+1):
    for j in range(1,C+1):
        data[i]+=d[j][i]
    data[i]+=data[i-1]
print(max(data))