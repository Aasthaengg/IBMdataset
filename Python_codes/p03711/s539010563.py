a = [0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
x, y = map(int, input().split())
x -= 1
y -= 1
if a[x] == a[y]:
    print("Yes")
else:
    print("No")
