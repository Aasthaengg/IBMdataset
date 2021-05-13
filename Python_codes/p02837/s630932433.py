#donut29
n=int(input())
lst=[]
for i in range(n):
    a=int(input())
    b=[]
    for j in range(a):
        x,y=map(int,input().split())
        x-=1
        b.append([x,y])
    lst.append(b)
ans=0
for i in range(2**n):
    on=[]
    switch=0
    for j in range(n):
        if ((i>>j)&1):
            on.append(j)
    for j in on:
        judge=lst[j]
        for k in judge:
            if k[1]==1:
                if not k[0] in on:
                    switch=1
            else:
                if k[0] in on:
                    switch=1
    if switch==0:
        ans=max(ans,len(on))

print(ans)