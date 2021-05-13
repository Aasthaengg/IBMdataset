X = list(map(int, input().split()))
sx = X[0]
sy = X[1]
tx = X[2]
ty = X[3]
x = tx - sx
y = ty - sy
l1 = "U" * y + "R" * x
l2 = "D" * y + "L" * x
l3 = "L" + "U" * (y + 1) + "R" * (x + 1) + "D"
l4 = "R" + "D" * (y + 1) + "L" * (x + 1) + "U"
print(l1 + l2 + l3 + l4)