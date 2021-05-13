import collections

H, W = map(int, input().split())
s = [list(input()) for i in range(H)]

z = [["b"] * W for _ in range(H)] #チェックしたマスはb(before)からa(after)にする
black = 0
for i in range(H):
    black += s[i].count("#") #最初の黒の数を数える
v = [[1,0], [0,1], [-1,0], [0,-1]] #動き方4パターン(↓ → ↑ ←)
que = collections.deque() #調べる候補リスト #調べ終わった要素は消す

#まず[0,0]
z[0][0] = "a"
s[0][0] = 1 #何歩で来れたかを代入していく #最初は1
que.append([0,0]) #最初の候補は[0,0]

#最短ルートを探す
while len(que) != 0: #候補がなくなるまで繰り返す
    i = que.popleft() #候補のうち1つを取り出し、リストから消す
    for dy, dx in v: #4パターンの動き方を考える
        y = i[0] + dy
        x = i[1] + dx
        if (0<=y<H and 0<=x<W and s[y][x]=="." and z[y][x]=="b"):
            z[y][x] = "a"
            s[y][x] = s[i[0]][i[1]] + 1
            que.append([y,x]) #進んだマスを新しく候補に入れる

if s[-1][-1] == ".": #[H,W]のマスに数字が入ってない→ゴールできない
    print(-1)
else: #「消せる白の最大数」=「全マス」-「黒マス」-「最短ルート」
    print(H*W - black - s[-1][-1])
