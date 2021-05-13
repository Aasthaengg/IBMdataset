n,m=map(int,input().split())
light=[]
ans=0
for i in range(m):
    List=list(map(int,input().split()))
    light.append(List)
p=list(map(int,input().split()))

for i in range(2**n):
    l=[0]*n
    for j in range(n):
        if (i>>j&1):
            l[j]=1
    on=0
    for k in range(m):
        cnt=0
        for o in range(1,len(light[k])):
            if (l[light[k][o]-1]==1):
                cnt+=1
        if cnt%2==p[k]:
            on+=1
    if on==m:
        ans+=1
print(ans)