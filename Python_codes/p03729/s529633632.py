a, b, c = input().split()

la = list(a)
lb = list(b)
lc = list(c)

# print(la[-1])
if la[-1] == lb[0] and lb[-1] == lc[0]:
    print('YES')
else:
    print('NO')