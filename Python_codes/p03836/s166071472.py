# coding = SJIS

sx, sy, tx, ty = map(int, input().split())
way = ""

for i in range(ty - sy):
    way += "U"
for i in range(tx - sx):
    way += "R"
for i in range(ty - sy):
    way += "D"
for i in range(tx - sx):
    way += "L"
way += "L"
for i in range(ty - sy + 1):
    way += "U"
for i in range(tx - sx + 1):
    way += "R"
way += "D"
way += "R"
for i in range(ty - sy + 1):
    way += "D"
for i in range(tx - sx + 1):
    way += "L"
way += "U"

print(way)