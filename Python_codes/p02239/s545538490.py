import sys
input = sys.stdin.readline

#入力と違って０オリジンとなっているので注意
n = int(input())
li = [[0] * n for _ in range(n)] #隣接行列、０オリジン li[i][j]:iからjへの有向グラフがある
for i in range(n):
    x, y, *v = [int(x)-1 for x in input().split()]
    for j in v:
        li[i][j] = 1 #有向グラフがあるところは１、ないところは０となる

from collections import deque
Q = deque([0]) #初期条件
finish = [0] #訪問済みの頂点をしまう
len_ = [-1]*n #頂点jの頂点０からの距離、できなかったらー１と返す
len_[0] = 0 #初期条件
while Q: #Qがからでない限り以下の操作を繰り返す
    i = Q.popleft()
    for j in range(n):
        if li[i][j] == 1: #iからjへの道が存在する場合
            if not j in finish: #まだjが探索済みじゃなかったら以下の操作を行う
                finish.append(j)
                Q.append(j)
                len_[j] = len_[i] + 1
        else:
            continue
for i in range(n):
    print(str(i+1) + ' ' + str(len_[i]))
