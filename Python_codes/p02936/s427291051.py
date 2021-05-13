n,q=map(int,input().split())
cnt=[0]*(n+1) #答えのリスト
lst=[[] for _ in range(n+1)] #連結リスト

for i in range(n-1):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in range(q):
    a,val=map(int,input().split())
    cnt[a]+=val

stack=[1]
visited=[None]*(n+1)
visited[1]=1
while stack:
    item=stack.pop()
    for i in lst[item]:
        if visited[i]==1:
            continue
        visited[i]=1
        stack.append(i)
        cnt[i]+=cnt[item]

print(" ".join(map(str,cnt[1:])))