r, c = map(int, input().split())

cc = [input() for i in range(r)]

from collections import deque


# 縦がｙ 横がx　だから座標はy,xて書く
st=[]
for i in range(r):
    for j in range(c):
        if cc[i][j]=="#":
            st.append([i,j])

# 保留スタックtodoにスタートの位置情報を入れる
todo=deque(st)
# 検知済みリストseenを-1で初期化 (何も検知してないてこと)
seen=[[-1 for i in range(c)] for j in range(r)]

# seenにはどんだけの手数でそこに到達できるかを入れる
# 例えばスタート地点は手数0でいけるから0を入れる
for i in range(len(st)):
    seen[st[i][0]][st[i][1]]=0

# 4方向の移動リスト これ使って移動していく
ido=[[1,0],[0,1],[-1,0],[0,-1]]
m=0
# 保留リストtodoが空になるまでやる
while todo:
    y, x=todo.popleft() # 現在地は保留からの先頭とりだす
    for i in range(4): # 現在地から4方向を見る
        ny, nx=y+ido[i][0], x+ido[i][1] # 現在地から隣の座標
        # 隣の座標が区画をはみ出さないかつ、検知してないときに
        if 0<=ny<r and 0<=nx<c and seen[ny][nx]==-1 and cc[ny][nx]!="#":
            # 隣に行けるということなので検知してその手数を格納
            seen[ny][nx]=seen[y][x]+1 # 手数＝前の地点の手数+1
            todo.append([ny,nx]) # 保留リストにも入れとく
            if seen[ny][nx]>=m:
                m=seen[ny][nx]
       

print(m)