d={}
for i in range(int(input())):
    d[i]={}
    a,b,c=map(int,input().split())
    if i==0:
        d[i][0]=a
        d[i][1]=b
        d[i][2]=c
    else:
        d[i][0]=max(d[i-1][1],d[i-1][2])+a
        d[i][1]=max(d[i-1][0],d[i-1][2])+b
        d[i][2]=max(d[i-1][1],d[i-1][0])+c
print(max(d[i][0],d[i][1],d[i][2]))