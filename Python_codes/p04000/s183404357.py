H, W , N = map(int,input().split())
from bisect import bisect_left
from bisect import bisect_right
matrix = []
for _ in range(N):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    matrix.append([x,y])
matrix.sort()
ans = [0 for _ in range(10)]
cand = {}
for l in matrix:
    for x_r in [-2, -1 , 0]:
        for y_r in [-2, -1 , 0]:
            nowx = l[0] + x_r
            nowy = l[1] + y_r
            if nowx < 0 or nowy < 0 or nowx + 2>= H or nowy+ 2 >= W:
                continue
            #ここで起点(左上)nowx, nowy として　 9マスに着目する
            name = str(nowx) + 'sakoda'  +str(nowy)
            try: cand[name] += 1
            except: cand[name] = 1
tmp = ((H - 2) * (W - 2))
for x in cand.values():
    ans[x] += 1
    tmp -= 1
ans[0] = tmp
for x in ans:
    print(x)
