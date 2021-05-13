def bellman_ford(s):
    d = [float('inf')]*n # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    for i in range(n):
        e=0
        for x, y, z in g:
            if d[y] > d[x] + z and d[x] != float('inf'):
                d[y] = d[x] + z
                e+=1
        # 負閉路が存在
                if i == n - 1 and y==n-1 :
                 return "inf"
    return (-1)*d[n-1]

n, m = map(int,input().split()) # n:頂点数, w:辺の数
g = []
for k in range(m):
    a, b, c = map(int,input().split()) # 始点,終点,コスト
    g.append([a-1, b-1, -c])
print(bellman_ford(0))