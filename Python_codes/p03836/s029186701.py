coordinates = list(map(int,input().split()))
s = []
t = []

for i in range(len(coordinates)):
    if i < 2:
        s.append(coordinates[i])
    else:
        t.append(coordinates[i])

# print(s)
# print(t)

dx = t[0] - s[0]
dy = t[1] - s[1]

route = ""

# print("dx: ", dx)
# print("dy: ", dy)

# 経路パターン１
# 行き
for i in range(dx):
    route += "R"
for i in range(dy):
    route += "U"

# 帰り
for i in range(dx):
    route += "L"
for i in range(dy):
    route += "D"

# 経路パターン２（パターン１の外側を通る）
# 行き
route += "D"

for i in range(dx+1):
    route += "R"
for j in range(dy+1):
    route += "U"

route += "L"
route += "U"

for i in range(dx+1):
    route += "L"
for i in range(dy+1):
    route += "D"

route += "R"


# 解答出力
print(route)