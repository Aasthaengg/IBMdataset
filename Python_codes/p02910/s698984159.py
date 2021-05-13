S = input()
for i, s in enumerate(list(S), 1):
    if (i % 2 == 0 and s == 'R') or (i % 2 == 1 and s == 'L'):
        print('No')
        break
else:
    print('Yes')
