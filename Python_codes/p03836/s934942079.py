sx,sy,tx,ty = list(map(int, input().strip().split()))
dx = tx-sx
dy = ty-sy
result = ""
for i in range(dy):
  result += "U"
for i in range(dx):
  result += "R"
for i in range(dy):
  result += "D"
for i in range(dx):
  result += "L"
result += "L"
  
for i in range(dy+1):
  result += "U"
for i in range(dx+1):
  result += "R"
result += "DR"
for i in range(dy+1):
  result += "D"
for i in range(dx+1):
  result += "L"
result += "U"
print(result)