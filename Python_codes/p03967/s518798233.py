s = input()

g = 0
p = 0

for si in s:
    if si == 'g':
        g += 1
    else:
        p += 1

print((g-p)//2)

