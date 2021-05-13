n, m = map(int, input().split())
d = {i: 0 for i in range(n)}
for i in range(m):
    a, b = map(int, input().split())
    d[a - 1] += 1
    d[b - 1] += 1
for i in d.values():
    if i % 2 == 1:
        print("NO")
        exit()
print("YES")