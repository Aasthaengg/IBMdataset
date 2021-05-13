# リストに格納する
l = []
lk = []
lv = []
n = int(input())
for _ in range(n):
    s, p = input().split()
    l.append(f"{s} {p}")
    lk.append(s)
    lv.append(int(p))


# リストを辞書に変換する
d = {}
for i in range(n):
    s, p = lk[i], lv[i]
    if s in d:
        d[s].append(p)
    else:
        d[s] = []
        d[s].append(p)


# 辞書をソートする・答えを出力する
d = dict(sorted(d.items()))
for k, v in d.items():
    d[k] = sorted(v, reverse=True)
    for i in d[k]:
        print(l.index(f"{k} {i}") + 1)