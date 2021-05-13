w, b = [int(i) for i in input().split()]

print("100 100")
a = []

for i in range(50):
    a.append(['#' for j in range(100)])

for i in range(50):
    a.append(['.' for j in range(100)])

for i in range(w - 1):
    x = (i % 50) * 2
    y = (i // 50) * 2 + 1
    a[y][x] = "."

for i in range(b - 1):
    x = (i % 50) * 2
    y = (i // 50) * 2 + 51
    a[y][x] = "#"

for y in range(100):
    print(''.join(a[y]))
