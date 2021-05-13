# D - Equals Union Find

N, M = map(int, input().split())
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(M)]

# 負ならそのノードが根かつ絶対値が木の要素数を示す、正なら値のノードが根であることを示す
root = [-1] * N 

# 木の高さを示す
rank = [1] * N

# インデックスxを与えると、xの根を返す関数
def find_root(x):
    if root[x] < 0:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]
    
# インデックスx,yを与えると、xとyの木を統合する関数
def union(x,y):
    # root_x, root_yは根のインデックス
    root_x = find_root(x)
    root_y = find_root(y)
    if root_x == root_y:
        return
    elif rank[root_x] > rank[root_y]: # 短い木(yの方)を長い木(xの方)に繋ぐ
        root[root_x] += root[root_y] # 要素数結合
        root[root_y] = root_x # 根を切り替え
    else:
        root[root_y] += root[root_x]
        root[root_x] = root_y
        
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1 # 新しい木の高さを1追加
            
for idx in range(M):
    union(xy[idx][0]-1, xy[idx][1]-1)
    
ans = 0
for i in range(N):
    if find_root(i) == find_root(p[i]-1):
        ans += 1
        
print(ans)