import collections

N = int(input())
tree = [[] for _ in range(N)] #i行目には、i番目のマスと隣り合っているマスの番号が加えられる
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

color = [0] * N #色が塗られていなければ0、黒は1、白は-1
color[0] = 1
color[N-1] = -1
que = collections.deque() #色が塗られたマスの番号を、隣り合うマスが全て塗られるまでここに入れる
que.append(0)
que.append(N-1)
while que: #塗るべきマスがなくなるまで繰り返す
    i = que.popleft() #「左から」が重要 #n回でたどり着けるマスはn回目に全て塗って良い
    for x in tree[i]:
        if color[x] == 0:
            color[x] = color[i]
            que.append(x) #塗ったマスは調べるリストに入れる

if sum(color) > 0: #合計が正、つまり黒が多い場合は先手の勝ち
    print("Fennec")
else: #合計が0でも先手の塗るマスがないため後手の勝ち
    print("Snuke")
