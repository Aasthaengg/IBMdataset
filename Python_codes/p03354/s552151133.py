from collections import deque
n,m=map(int,input().split())
p=list(map(int,input().split()))
ab=[[] for _ in range(n+1)]
ab_dict={}
count=0
for i in range(1,n+1):
    ab_dict[p[i-1]]=i
    if p[i-1]==i:
        count+=1
for i in range(m):
    a,b=map(int,input().split())
    ab[a].append(b)
    ab[b].append(a)
visited=[1]+[0]*(n)
su=[]
for i in range(1,n+1):
    if visited[n]==0:
        temp=set()
        temp.add(i)
        stack=deque()
        stack.append(i)
        visited[i]+=1
        while stack:
            x=stack.pop()
            for j in ab[x]:
                if visited[j]==0:
                    visited[j]+=1
                    stack.append(j)
                    temp.add(j)
        su.append(temp)

for k in su:
    for l in k:
        if ab_dict[l] in k and ab_dict[l]!=l:
            count+=1
print(count)