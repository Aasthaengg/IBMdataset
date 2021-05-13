N, u, v = map(int, input().split())
L = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    L[a - 1].append(b - 1)
    L[b - 1].append(a - 1)

Leaf = []  # 葉かどうかを記録する
for i in range(N):
    c = 0
    for j in L[i]:
        c = c + 1
    if c == 1:
        Leaf.append(True)
    else:
        Leaf.append(False)

UD = [0 for i in range(N)]  # 各頂点のuからの距離
UD[u - 1] = -1  # 0でないなら訪問済みとする
M = L[u - 1]  # 次に訪れるノードのリスト
d = 1  # uからの距離
while True:
    new_M = []
    for i in M:
        if UD[i] == 0:  # 0 ならiに隣接するノードをnew_Mに追加
            UD[i] = d
            for j in L[i]:
                new_M.append(j)
        else:
            pass
    M = new_M
    if len(M) == 0:
        break
    d = d + 1
UD[u-1] = 0

VD = [0 for i in range(N)]
VD[v-1] = -1
M = L[v-1]
d = 1

while True:
    new_M = []
    for i in M:
        if VD[i] == 0:  # 0 ならiに隣接するノードをnew_Mに追加
            VD[i] = d
            for j in L[i]:
                new_M.append(j)
        else:
            pass
    M = new_M
    if len(M) == 0:
        break
    d = d + 1
VD[v-1] = 0




d = -1
index = u-1
# vよりもuの方が近く,最もvから離れている葉を見つける
for i in range(N):
    if Leaf[i]:
        if UD[i] < VD[i]:
            if d < VD[i]:
                d = VD[i]

print(d-1)







