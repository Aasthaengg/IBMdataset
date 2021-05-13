# ＤＦＳ, パターン列挙_竹'n'本の使用パターン
'''
from collections import deque

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

queue = deque([[0],[1],[2],[-1]]) # 初期化_ここでは竹の使用パターン4つを設置
ptns = [] # パターン候補の器_初期化
 
while queue: # stackが空になるまでループ
    tmp = queue.pop() # パターンの候補を pop
    if len(tmp) == n: # 条件に合えば append
        ptns.append(tmp)
    elif len(tmp) < n: # 条件に合わなければ...
        w = tmp + [0] # パターンの候補を作成して...
        x = tmp + [1] # 〃
        y = tmp + [2] # 〃
        z = tmp + [-1]
        queue += [w, x, y, z]  # 積む

#print(ptns) # 竹の使用パターン

ans = 10**9
for i in range(len(ptns)):
    if 0 not in ptns[i] or 1 not in ptns[i] or 2 not in ptns[i]:
        continue
    abc = [0, 0, 0, -30]
    for j in range(n):
        tmp = ptns[i][j]
        if tmp >= 0:
            abc[tmp] += l[j]
            abc[3] += 10
    mp = abc[3]
    mp += abs(abc[0] - a)
    mp += abs(abc[1] - b)
    mp += abs(abc[2] - c)
    ans = min(ans, mp)

print(ans)

'''
# パターン列挙と探索を並行して処理

from collections import deque

n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

queue = deque([[0],[1],[2],[-1]])

ans = 10**9
while queue:
    tmp = queue.pop()
    if len(tmp) == n:
        if 0 not in tmp or 1 not in tmp or 2 not in tmp:
            continue
        abc = [0, 0, 0, -30]
        for j in range(n):
            if tmp[j] >= 0:
                abc[tmp[j]] += l[j]
                abc[3] += 10
        mp = abc[3]
        mp += abs(abc[0] - a)
        mp += abs(abc[1] - b)
        mp += abs(abc[2] - c)
        ans = min(ans, mp)

    elif len(tmp) < n:
        w = tmp + [0]
        x = tmp + [1]
        y = tmp + [2]
        z = tmp + [-1]
        queue += [w, x, y, z]

print(ans)
