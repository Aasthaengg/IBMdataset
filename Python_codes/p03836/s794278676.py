sx,sy,tx,ty = map(int,input().split())
# 距離 s < tより
dx = tx - sx
dy = ty - sy

res = ""
# 1回目
# いきし
for i in range(dx):
    res += "R"
for i in range(dy):
    res += "U"
# かえりし
for i in range(dx):
    res += "L"
for i in range(dy):
    res += "D"

# 2回目
# いきし 1回上に上がる dx + 1いく
res += "D"
for i in range(dx+1):
    res += "R"
for i in range(dy+1):
    res += "U"
res += "L"
# かえりし 1回下がっとく
res += "U"
for i in range(dx+1):
    res += "L"
for i in range(dy+1):
    res += "D"
res += "R"
print(res)
