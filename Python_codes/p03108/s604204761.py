# cnt->size
N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]
AB.reverse()    # 逆から考える

ans_list = [-1 for i in range(M)]
ans_list[M-1] = N*(N-1)//2

# parent(親)
par = [i for i in range(N+1)]
# rank(深さ)
rank = [0 for i in range(N+1)]
# 同グループの頂点数
size = [1 for i in range(N+1)]

# 木の根を求める
def root(x):
    if par[x] == x:             # 根の時
        return x
    else:
        par[x] = root(par[x])   # 経路圧縮
        return par[x]

# xとyの属する集合を併合(ランク有)
def unite(x,y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
        size[y] += size[x]
    else:
        par[y] = x
        size[x] += size[y]
        if rank[x] == rank[y]:
            rank[x] += 1

for i in range(M-1):
    a,b = AB[i][0],AB[i][1]
    # 答えはans_list[M-2-i]を書き換える
    if root(a) == root(b):
        ans_list[M-2-i] = ans_list[M-1-i]
        continue
    else:
        ans_list[M-2-i] = ans_list[M-1-i] - size[root(a)]*size[root(b)]
        unite(a,b)
print('\n'.join(map(str,ans_list)))

