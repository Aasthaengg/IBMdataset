#Equals
n,m=map(int,input().split())
p=list(map(int,input().split()))
p=[0]+p
data=[[] for _ in range(n+1)]
flag=[0]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    data[x].append(y)
    data[y].append(x)
tree=[0]*(n+1)
for i in range(1,n+1):
    if flag[i]==0:
        que=[i]
    while que:
        h=que.pop()
        flag[h]=1
        tree[h]=i
        for u in data[h]:
            if flag[u]==0:
                que.append(u)
count=0
for i in range(1,n+1):
    if tree[i]==tree[p[i]]:
        count+=1
print(count)