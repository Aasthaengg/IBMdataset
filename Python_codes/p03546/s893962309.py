h, w = map(int, input().split())
maptrans = []
for i in range(10):
    l = list(map(int, input().split()))
    maptrans.append(l)
costtoone = []
# ダイレクトに1に行くときのコスト
for i in range(10):
    costtoone.append(maptrans[i][1])

for loop in range(10): # 念のためループ
    for tonum in range(10): # この数経由
        for i in range(10):
            costtoone[i] = min(costtoone[i], costtoone[tonum] + maptrans[i][tonum])

#print(costtoone)


maze = []
for hh in range(h):
    l = list(map(int, input().split()))
    maze.append(l)

res = 0
for hh in range(h):
    for ww in range(w):
        if maze[hh][ww] == 1 or maze[hh][ww] == -1:
            continue
        #print(maze[hh][ww], "=" ,costtoone[maze[hh][ww]])
        res += costtoone[maze[hh][ww]]
print(res)
