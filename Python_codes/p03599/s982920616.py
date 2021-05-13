A,B,C,D,E,F = map(int, input().split())

can = []
for i in range(0, F + 1, 100 * A):
    for j in range(0, F - i + 1, 100 * B):
        water = i + j

        for k in range(0, F - water + 1, C):
            for l in range(0, F - water - k + 1, D):
                salt = k + l
                
                can.append((water, salt))

# (water, salt)
ans = (100 * A, 0)
noudo = 0
for water, salt in can:
    if water == salt == 0: continue

    if (water / 100) * E >= salt:
        tmp = 100 * salt / (water + salt)
        if noudo < tmp:
            ans = (water, salt)
            noudo = tmp

print(sum(ans), ans[1])