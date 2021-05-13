c = []
for i in range(3):
    x, y, z = map(int, input().split())
    c.append(x)
    c.append(y)
    c.append(z)

for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1 = c[0] - a1
            b2 = c[1] - a1
            b3 = c[2] - a1
            if c[3] == a2 + b1 and c[4] == a2 + b2 and c[5] == a2 + b3 and c[6] == a3 + b1 and c[7] == a3 + b2 and c[8] == a3 + b3:
                print('Yes')
                exit()
print('No')
