def dfs(f):
    if vis[f] == 1:
        return
    vis[f] = 1 #fを訪問済にする
    for t in v[f]: #fとつながっている頂点を読み込む
        if f != a or t != b: #(a,b)の組み合わせでなければ繰り返す
            dfs(t)

n, m = map(int, input().split())
v = [[] for i in range(n)]
e = []

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)
    e.append([a, b])

ans = 0

for a, b in e:
    vis = [0]*n
    dfs(a)
    if vis[b] == 0: #aからa-bの辺以外を辿ってbに行けるなら1になる
        ans += 1

print(ans)
