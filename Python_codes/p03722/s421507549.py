def shortest_path(s,n,w,es):
#s→iの最短距離
# s:始点, n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [float('inf')] * n
    #d[i] : s→iの最短距離
    d[s] = 0
    while True:
        for p,q,r in es:
        # e: 辺iについて [from,to,cost]
            #print(d,p,q,r)
            if d[p] != float('inf') and d[q] > d[p] + r:
                d[q] = d[p] + r
                update = True
            ans1=d[-1]
        update = False
        for p,q,r in es:
        # e: 辺iについて [from,to,cost]
            #print(d,p,q,r)
            if d[p] != float('inf') and d[q] > d[p] + r:
                d[q] = d[p] + r
            ans2=d[-1]
        return -ans1 if ans1==ans2 else 'inf' 
################
n,w = map(int,input().split()) #n:頂点数　w:辺の数
es = [] #es[i]: [辺の始点,辺の終点,辺のコスト]
for _ in range(w):
 x,y,z = map(int,input().split())
 es.append([x-1,y-1,-z])
print(shortest_path(0,n,w,es))