t = [0, 0, 0, 0]

for i in range(3):
    a, b = map(int, input().split())
    t[a - 1] += 1
    t[b - 1] += 1
print("NO" if 3 in t else "YES")