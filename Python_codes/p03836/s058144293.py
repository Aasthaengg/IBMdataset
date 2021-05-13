sx, sy, tx, ty = map(int, input().split())
x = tx - sx
y = ty - sy
ans = ("R" * x + "U" * y + "L" * x + "D" * y + "D" + "R" * -~x + "U" * -~y +
       "L" + "U" + "L" * -~x + "D" * -~y + "R")
print(ans)
