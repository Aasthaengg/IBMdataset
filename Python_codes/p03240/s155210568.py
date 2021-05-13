import sys

# 解説カンニング済み

N = int(input())
xs = []
ys = []
hs = []
reference = None
for i in range(N):
    x, y, h = map(int, input().split())
    xs.append(x)
    ys.append(y)
    hs.append(h)
    # 地面でないことが分かっている(ピラミッド内のサンプル)を1つ選ぶ
    if h > 0:
        reference = (x, y, h)

for cx in range(0, 100+1):
    for cy in range(0, 100+1):
        # サンプルの高さを求める
        rx, ry, rh = reference
        ref_H = rh + abs(rx-cx) + abs(ry-cy)
        # 他のデータも全てサンプルと合致するか検証する
        ok = True
        for i in range(N):
            calc_H = max(ref_H - abs(xs[i]-cx) - abs(ys[i]-cy), 0)
            if calc_H != hs[i]:
                ok = False
                break
        if ok:
            print(cx, cy, ref_H)
            sys.exit(0)
