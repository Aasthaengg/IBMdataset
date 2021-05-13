S = input()

i = 0
for l in S:
    if l == 'C':
        i = 1
    if i == 1 and l == 'F':
        print('Yes')
        exit()

print('No')
