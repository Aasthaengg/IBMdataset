def bellman_ford(s):
    d = [-float("inf")]*n # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    check = [False]*n
    for i in range(n):
        update = False # 更新が行われたか
        for x, y, z in g:
            if d[y] < d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        # 負閉路が存在
        if i == n - 1:
          for x, y, z in g:
            if d[y] < d[x] + z:
                d[y] = d[x] + z
                check[x]=True
                check[y]=True
    if check[n-1]:
      return "inf"
    return d[n-1]

n, w = [int(x) for x in input().split()] # n:頂点数, w:辺の数
g = []
for _ in range(w):
    x, y, z = [int(x) for x in input().split()] # 始点,終点,コスト
    g.append([x-1, y-1, z])
    #g.append([y, x, z]) # 有向グラフでは削除
print(bellman_ford(0))