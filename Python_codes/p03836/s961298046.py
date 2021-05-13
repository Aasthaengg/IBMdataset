sx,sy,tx,ty = map(int,input().split())
x_move = tx - sx
y_move = ty - sy
ans = ""
for i in range(x_move):
  ans += "R"
for j in range(y_move):
  ans += "U"
for a in range(x_move):
  ans += "L"
for b in range(y_move):
  ans += "D"
ans += "L"
for i in range(y_move + 1):
  ans += "U"
for i in range(x_move + 1):
  ans += "R"
ans += "D"
ans += "R"
for i in range(y_move + 1):
  ans += "D"
for i in range(x_move + 1):
  ans += "L"
ans += "U"
print(ans)