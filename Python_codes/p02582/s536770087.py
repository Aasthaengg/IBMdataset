S = input().rstrip()
num = 0
mnum = 0
for c in S:
    if c == 'R':
        num += 1
    else:
        num = 0

    if mnum < num:
        mnum = num

print(mnum)
