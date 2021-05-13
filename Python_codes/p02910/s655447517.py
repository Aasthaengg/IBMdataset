S = input()
for i, s in enumerate(S, 1):
    if i % 2 == 1:
        if s == 'L':
            print('No')
            break
    else:
        if s == 'R':
            print('No')
            break
else:
    print('Yes')
