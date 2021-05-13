sx,sy,tx,ty = map(int,input().split())
y_diff = ty-sy
x_diff = tx-sx
ans = ""
for i in range(y_diff):
    ans += "U"
for j in range(x_diff):
    ans += "R"
for k in range(y_diff):
    ans += "D"
for l in range(x_diff):
    ans += "L"
ans += "L"
for s in range(y_diff+1):
    ans += "U"
for t in range(x_diff+1):
    ans += "R"
ans += "DR"
for p in range(y_diff+1):
    ans += "D"
for q in range(x_diff+1):
    ans += "L"
ans+="U"
print(ans)