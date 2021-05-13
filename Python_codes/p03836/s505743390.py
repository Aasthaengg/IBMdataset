sx, sy, tx, ty = map(int, input().split())

W = abs(sx-tx)
H = abs(sy-ty)
ans = ""

for i in range(W):
    ans += "R"
for i in range(H+1):
    ans += "U"
for i in range(W+1):
    ans += "L"
for i in range(H+1):
    ans += "D"
ans += "R"

for i in range(H):
    ans += "U"
for i in range(W+1):
    ans += "R"
for i in range(H+1):
    ans += "D"
for i in range(W+1):
    ans += "L"
ans += "U"

print(ans)
