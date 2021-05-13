from collections import deque
n,q=map(int,input().split())
tree=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a) # 無向グラフなので
ans=[0]*n
for _ in range(q):
    p,x=map(int,input().split())
    ans[p-1]+=x

stack=deque([[0,-1]]) # 根の位置、現位置の元になる根
visited=[0]*n
visited[0]=1

while stack:
    cur,rot=stack.pop()
    for i in tree[cur]:
        if visited[i]==0 and i!=rot:
            visited[i]=1
            ans[i]+=ans[cur]
            stack.append([i,cur])
print(*ans)