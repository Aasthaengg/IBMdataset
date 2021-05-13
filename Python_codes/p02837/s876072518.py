n=int(input())
said=[]
for i in range(n):
    a=int(input())
    said.append([list(map(int,input().split())) for _ in range(a)])
ans=0
for i in range(2**n):
    l=[0]*n
    for j in range(n):
        if (i>>j&1):
            l[j]=1
    flag=True
    for k in range(n):
        if l[k]==1 and (not all(said[k][x][1]==l[said[k][x][0]-1] for x in range(len(said[k])))):
            flag=False
            break
    if flag==True and l.count(1)>ans:
        ans=l.count(1)
print(ans)