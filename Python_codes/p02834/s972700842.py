#ABC148-F Playing Tag on Tree
"""
与えられるグラフは木構造
青木くん(追いかける方)がいる頂点を根とすると、この問題は解きやすくなる。
そうした場合、高橋くんが追いつかれずに行ける頂点の中で、最も深さが深い葉に行くのが最適。
そのような頂点は頂点u,vからの距離によって求めることができ、結果的に高橋くんが行ける最深部の葉から
根までの距離が答えとなる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,u,v = map(int,readline().split())
u,v = u-1,v-1 #u:高橋くん初期位置,v:青木くん初期位置

g = [[] for _ in range(n+1)] #隣接リスト
for i in range(n-1):
    a,b = map(int,readline().split())
    a,b = a-1,b-1
    g[a].append(b)
    g[b].append(a)

#根からの距離を記録
#rank:rootからの距離
root = v
rank = [0]*n
new = [root] #深さを揃えて探索する必要があるのでstackとは若干異なる
c = 1
while len(new):
    tank = []
    for e in new:
        for go in g[e]:
            if go != root and rank[go] == 0:
                rank[go] = c
                tank.append(go)
    c += 1
    new = tank

#まず、高橋くんが最大でどの頂点まで戻れるのかを求める
now = u
res = rank[u]-(rank[u]-1)//2 #制限は(u-g間の距離-1)//2
ans = (rank[u]-1)//2 #戻れる最大の回数をansに入れる
while True:
    for e in g[now]:
        if rank[e] < rank[now]:
            if rank[e] < res: #制限より大きいならそこには行けない
                break
            else:
                now = e #nowに戻れる最大の頂点を格納
        else:
            continue
    if rank[e] < res: #制限より大きいならそこには行けない
        break

#ans + nowからの最大の深さが答え。
new = [now]
while new:
    tank = []
    for e in new:
        for go in g[e]:
            if rank[go] > rank[e]: #深さが増すなら
                tank.append(go)
    ans += 1
    new = tank

print(ans-1 if rank[u]%2==1 else ans)