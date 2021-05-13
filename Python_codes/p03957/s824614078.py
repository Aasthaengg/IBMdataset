S = input()
a = 0
for s in S:
    if a == 0 and s == 'C':
        a += 1
    if a == 1 and s == 'F':
        print('Yes')
        exit()
print('No')