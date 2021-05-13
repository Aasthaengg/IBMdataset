n = list(map(int, input().split()))
p = n[0]
q = n[1]
r = n[2]

x = p + q
y = q + r
z = r + p

print(min(x, y, z))