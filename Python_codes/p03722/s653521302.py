n, m = map(int, input().split())
g = []
for _ in range(m):
    a, b, c = map(int, input().split())
    g.append([a - 1, b - 1, -c])

def bellman_ford(s):
    d = [float('inf')]*n # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    flg = False
    for i in range(n):
        update = False # 更新が行われたか
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
        if i == n - 1:
            inf_flg = d[-1]
            flg = True
    if flg:
        for i in range(n):
            update = False # 更新が行われたか
            for x, y, z in g:
                if d[y] > d[x] + z:
                    d[y] = d[x] + z
                    update = True
            if not update:
                break
            if i == n - 1:
                if inf_flg != d[-1]:
                    return "inf"
    return -1 * d[-1]

print(bellman_ford(0))