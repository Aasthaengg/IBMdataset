r, d, x = map(int, input().split())
y = [x]
for i in range(10):
    y.append(r * y[i] - d)
    print(r * y[i] - d)