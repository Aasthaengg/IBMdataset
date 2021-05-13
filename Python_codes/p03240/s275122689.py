import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())  #空白あり

N = I()
xyh = [tuple(MI()) for i in range(N)]

for i in range(101):  # ピラミッドの中心座標のx座標
    for j in range(101):  # ピラミッドの中心座標のy座標
        for k in range(N):
            x,y,h = xyh[k]
            if h != 0:
                H = h + abs(x-i) + abs(y-j)
                break
        for k in range(N):
            x,y,h = xyh[k]
            if h != max(H - abs(x-i) - abs(y-j),0):
                break
        else:
            print(i,j,H)
            exit()
