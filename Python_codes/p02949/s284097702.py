def bellmanford(v,s,path):
    # 距離をinfで初期化
    d = [float('inf')]*v

    # startの頂点までの距離 = 0
    d[s] = 0
    for j in range(v):
        update = False

        # 各頂点までの距離を更新
        # 全辺について、"頂点bまでの距離"が"aまでの距離"+"aからbまでの辺"よりも大きいとき更新
        for a,b,c in path:
            if d[b] > d[a] + c:
                d[b] = d[a] + c
                update = True

        # 更新が行われない場合はやめる。
        if not update:
            break
        # 負の閉路の検出。負の閉路を求めないならいらない。
        # v-1回更新しても、さらに更新できるときは負の閉路が存在することになる。
        elif j == v-1:
            return -1

    return d

n,m,p = map(int,input().split())

path = [[] for i in range(n)]
path_inv = [[] for i in range(n)]

for i in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    c-=p
    path[a].append([b,-c])
    path_inv[b].append([a,-c])

a = [0]*n
s = 0
a[0]=1
stack = [s]
while stack:
    p = stack.pop()
    for q,r in path[p]:
        if a[q]==0:
            a[q]=1
            stack.append(q)

b = [0]*n
g = n-1
b[n-1]=1
stack = [g]
while stack:
    p = stack.pop()
    for q,r in path_inv[p]:
        if b[q]==0:
            b[q]=1
            stack.append(q)

c = [i for i in range(n) if a[i]==b[i]==1]

path2 = []
for i in c:
    for to,cost in path[i]:
        path2.append([i,to,cost])

d = bellmanford(n,0,path2)
if d==-1:
    print(-1)
else:
    print(max(0,-d[-1]))