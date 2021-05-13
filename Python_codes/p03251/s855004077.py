n, m, x, y = map(int, input().split())
xs = input().split()
ys = input().split()

for i in range(n):
    xs[i] = int(xs[i])

for i in range(m):
    ys[i] = int(ys[i])

for i in range(x+1, y+1):
    if i > max(xs) and i <= min(ys):
        print("No War")
        exit()

print("War")
