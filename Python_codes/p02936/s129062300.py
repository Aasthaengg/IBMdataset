from collections import deque
n,q=map(int,input().split())
count=[0]*(n+1)
ab=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    ab[a].append(b)
    ab[b].append(a)
for _ in range(q):
    p,x=map(int,input().split())
    count[p]+=x
stack=[]
visited=[0]*(n+1)
stack.append(1)
visited[1]=1
while stack:
    y=stack.pop()
    for i in ab[y]:
        if visited[i]==0:
            visited[i]+=1
            count[i]+=count[y]
            stack.append(i)
for j in range(n+1):
    count[j]=str(count[j])
print(" ".join(count[1:]))