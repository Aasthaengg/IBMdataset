n, x = map(int, input().split())
l = list(map(int, input().split()))
# ボールが跳ねる座標の数列を作成する。
# 初期値は、0である。
d = [0]
for i in range(n):
    d.append(d[i]+l[i])
a = 0
for dd in d:
  	# ボールが何回、跳ねるかどうか？
    # X座標以下である座標は跳ねるので、カウントする。
    if dd <= x:
        a += 1
print(a)
