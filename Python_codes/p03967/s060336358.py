s = input().rstrip()

gc = 0
pc = 0
ts = 0
ds = 0
for si in s:
    if si == 'g':
        if pc < gc:
            ds += 1
            pc += 1
        else:
            gc += 1
    else:
        if pc < gc:
            pc += 1
        else:
            gc += 1
            ts += 1

print(ds - ts)