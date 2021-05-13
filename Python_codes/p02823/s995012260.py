n,a,b = map(int, input().split())

#距離
d = b-a
c = 0
if d % 2 == 0:
    c = d // 2
else:
    # 端っこに近い方に行く
    c = min(n-b, a-1)
    # 一試合距離を縮める
    c += 1
    d -= 1
    # お互い近づく
    c += (d // 2)

print(c)