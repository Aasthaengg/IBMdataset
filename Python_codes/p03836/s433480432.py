sx, sy, tx, ty = map(int, input().split())

tx_sx = tx - sx
ty_sy = ty - sy


ans = ""
for i in range(ty_sy):
    ans += "U"

for i in range(tx_sx):
    ans += "R"


for i in range(ty_sy):
    ans += "D"

for i in range(tx_sx):
    ans += "L"

ans += "L"

for i in range(ty_sy + 1):
    ans += "U"

for i in range(tx_sx + 1):
    ans += "R"
ans += "DR"

for i in range(ty_sy + 1):
    ans += "D"

for i in range(tx_sx + 1):
    ans += "L"

ans += "U"
print(ans)
