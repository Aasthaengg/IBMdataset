n,m=map(int,input().split())
light=[list(map(int,input().split())) for _ in range(m)]
p=list(map(int,input().split()))
ans=0
for i in range(2**n):
    state=[0]*n
    for j in range(n):
        if (i>>j&1):
            state[j]=1
    light_num=0
    for k in range(m):
        switch_num=0
        for l in range(1,light[k][0]+1):
            if state[light[k][l]-1]==1:
                switch_num+=1
        if switch_num%2==p[k]:
            light_num+=1
    if light_num==m:
        ans+=1
print(ans)