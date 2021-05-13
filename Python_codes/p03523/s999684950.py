S = input()

AKB = 'AKIHABARA'
AKBL = list(AKB)

bits = []
for i in range(2 ** 4):
    b = format(i, 'b').zfill(4)
    bits.append(b)

# print(bits)

ss = []
for bi in bits:
    s = AKBL.copy()
    for i, b in enumerate(bi):
        if b == '1':
            if i == 0:
                s[0] = None
            elif i == 1:
                s[4] = None
            elif i == 2:
                s[6] = None
            elif i == 3:
                s[8] = None
    s = "".join([c for c in s if c is not None])
    ss.append(s)

if S in ss:
    print('YES')
else:
    print('NO')