s = input()

res = 0
g_stock = 0
for i in s:
    if i == 'g':
        g_stock += 1
    else:
        if g_stock > 0:
            g_stock -= 1
        else:
            res -= 1
res += g_stock//2
print(res)

