# ワーシャルフロイド法
n,w = map(int,input().split()) #n:頂点数　w:辺の数

d = [[float("inf") for i in range(n)] for i in range(n)] 

# 入力の辺リスト
e_list = []
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(w):
    x,y,z = map(int,input().split())
    d[x-1][y-1] = z
    d[y-1][x-1] = z
    # 入力の辺リストに追加
    e_list.append([x-1,y-1,z])
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
    
#d[i][j]: iからjへの最短距離
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j],d[i][k] + d[k][j])

# 移動コスト表示
#print(d)
##############################

# 辺の数から使用済みの数を引く
ans = w
for x, y, z in e_list:
    # dにx,y,z の情報が残っていたら利用されている
    if d[x][y] == z:
        ans -= 1
        
print(ans)