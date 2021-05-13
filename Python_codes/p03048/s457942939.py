r, g, b, n = map(int, input().split())

l = sorted([r, g, b])
x = l[0]
y = l[1]
z = l[2]

ans = 0

mz = n // z
for i in range(mz + 1):
    my = (n - z * i) // y
    for j in range(my + 1):
        if (n - z * i - y * j) % x == 0:
            ans += 1

print(ans)
