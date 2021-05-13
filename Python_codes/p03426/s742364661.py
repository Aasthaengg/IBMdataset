h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

iti = [[] for _ in range(h*w + 1)]

for h_ in range(h):
    for w_ in range(w):
        iti[a[h_][w_]].append(w_+1)
        iti[a[h_][w_]].append(h_+1)

#累積和的なやつ
s_d = [[] for _ in range(d+1)]
for i in range(1, d+1): # i:= スタート位置　1からｄまである
    now = i
    s_d[i].append(0) # スタート位置のコストは０
    while now + d <= h*w:
        s_d[i].append(s_d[i][-1] + abs(iti[now][0]-iti[now+d][0]) + abs(iti[now][1]-iti[now+d][1]))
        now += d
#print(s_d)

def query(l, r):
    idx = l % d # スタート位置 = idx　
    if idx == 0:
        idx = d
    # s_d[idx]の配列を使用
    # l, rをs_d[idx]上のインデックスに合わせる
    l_d = l // d
    r_d = r // d
    if l % d == 0:
        l_d -= 1
        r_d -= 1
    cost = s_d[idx][r_d] - s_d[idx][l_d]
    return cost


q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(query(l, r))
