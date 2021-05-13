n,m=map(int,input().split())
p = [int(i)-1 for i in input().split() ]


tree=[[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

from collections import deque

groups=[]
been=[0]*n
for i in range(n):
    if been[i]==0:
        group=[i]
        been[i]=1
        q = deque([(i,togo) for togo in tree[i]]) 
        while q:
            parent,x = q.popleft()
            if been[x]==1:
                continue
            been[x]=1
            group.append(x)
            for y in tree[x]:
                if y == parent:#親ノードを飛ばし
                    continue
                q.append((x,y))#子ノードを追加
        groups.append(group)

ans=0
for group in groups:
    ans+= len( set(group) & set(p[g] for g in group) )

print(ans)