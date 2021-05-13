s = input()
for c in 'abcdefghijklmnopqrstuvwxyz':
    if c not in s:
        print(c)
        exit()
print('None')