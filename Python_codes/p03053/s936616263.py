from collections import deque
import sys
input = sys.stdin.readline #inputの際に入力が終わるまで読み続ける


##入力例1
# 3 3
# ...
# .#.
# ...
def search():
    H, W = map(int, input().split()) ##H=3,W=3
    pos = deque([])

    D = [[True] * (W + 2)]  # True True True True True
    D += [[True] + [False] * W + [True] for i in range(H)]  # True False False False True
    D.append([True] * (W + 2))  # True True True True True
    ## T T T T T
    ## T F F F T
    ## T F F F T
    ## T F F F T
    ## T T T T T

    for i in range(H):
        maze = input() #inputの際に入力が終わるまで読み続ける
        for j in range(W):
            if maze[j] == "#":
                pos.append([i + 1, j + 1, 0]) #pos = ([2, 2, 0])
                D[i + 1][j + 1] = True
    ## T T T T T
    ## T F F F T
    ## T F T F T
    ## T F F F T
    ## T T T T T

    while len(pos) > 0:
        h, w, depth = pos.popleft()
        ##上下左右の座標に同時進行で同じ操作を行う

        if not D[h + 1][w]: #([2, 2, 0])の一つ上の座標([3, 2, 0])がNot True(False)の場合
            pos.append([h + 1, w, depth + 1]) #その座標([3, 2, 1])をpopに追加
                                              #deathは黒を白に変更した回数を記録していく
            D[h + 1][w] = True #その座標([3, 2, 0])をTrueに変更

        if not D[h - 1][w]:
            pos.append([h - 1, w, depth + 1])
            D[h - 1][w] = True

        if not D[h][w + 1]:
            pos.append([h, w + 1, depth + 1])
            D[h][w + 1] = True

        if not D[h][w - 1]:
            pos.append([h, w - 1, depth + 1])
            D[h][w - 1] = True
    ##最終的なdeath(白を黒に変更した回数)を出力
    return depth


print(search())




