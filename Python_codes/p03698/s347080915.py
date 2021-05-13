S = input()

mem = {}

for c in S:
    if c in mem.keys():
        print('no')
        exit()
    else:
        mem[c] = 1
print('yes')