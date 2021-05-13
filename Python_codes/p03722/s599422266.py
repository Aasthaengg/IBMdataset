n,m=map(int,input().split())

def bellman_ford(v, s, e):
    INF = 10**18
    # コストをINFで初期化
    d = [INF] * v
    # 開始頂点は0
    d[s] = 0
    # 負の閉路が無ければ更新はV-1回までで終わる
    for i in range(v):
        f = False
        for a, b, c in e:
            if d[a]==INF:continue
            # aまでのコスト+辺abのコストがbまでのコストより小さければ更新
            cost = d[a] + c
            if cost < d[b]:
                d[b] = cost
                f = True
                if i==v-1 and b==v-1:
                    return -1
        # 更新が無ければbreak
        if not f:
            break

    return d
e=[]
for i in range(m):
    a,b,c=[int(j) for j in input().split()]
    e.append((a-1,b-1,-c))

ans=bellman_ford(n,0,e)
if ans==-1:
    print("inf")
else:
    print(-ans[-1])




