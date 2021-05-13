r, d, x = map(int, input().split())

t = r*x - d
print(t)
for i in range(9):
    t = r*t - d
    print(t)