#f
N,U,V = map(int,input().split())
U-=1
V-=1
tree =[[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    tree[a].append(b)
    tree[b].append(a)

from collections import deque
def shortest(tree,start):
    from_start=[None]*N
    q = deque([(-1,start,0)])
    while q:
        parent,x,time = q.popleft()
        if tree[x]==[parent] or (len(tree[x])==1 and parent==-1):#行き先が親しかない＝＝葉ノード
            from_start[x]=time
        for y in tree[x]:
            if y == parent:#親ノードを飛ばし
                continue
            q.append((x,y,time+1))#子ノードを追加
    return from_start

from_u = shortest(tree,U)
from_v = shortest(tree,V)

print( max([vv for uu,vv in zip(from_u,from_v) 
            if isinstance(uu, int) and isinstance(vv, int) and uu<vv])-1 )