import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

l = []

for i in range(N):
    v = list(map(int, input().split()))
    l.append(v)

    # 高さ0の時は下で使う式変形が成り立たないので、高さがある時のものを使う。
    # 全部0のパターンはありえない。なぜなら全部0としたとき、高さが1で調査していない座標を中心としたものが複数条件を
    # 満たしてしまうので、中心が一個に特定されるという条件に反するため。
    if v[2]:
        x,y,h = v[0], v[1], v[2]

for X in range(101):
    for Y in range(101):
        H = h + abs(x-X) + abs(y-Y)
        if all(h == max(H - abs(x-X) - abs(y-Y), 0) for x,y,h in l):
            print(X,Y,H)
            exit()