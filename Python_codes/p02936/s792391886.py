from collections import deque
n,q=map(int,input().split())
tree=[[] for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)
cnt=[0]*n
for i in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x

stack=deque([[0,0,-1]]) # 現在地、その位置で引き継いできたcount、前の位置

while stack:
    num,count,preb = stack.pop()
    cnt[num]+=count
    for i in tree[num]:
        if i == preb:
            continue
        stack.append([i,cnt[num],num])

print(*cnt)