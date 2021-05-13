S = input()
ki = 'RUD'
gu = 'LUD'
for i, s in enumerate(S):
    if i%2 == 0:
        if s not in ki:
            print('No')
            exit()
    else:
        if s not in gu:
            print('No')
            exit()
print('Yes')