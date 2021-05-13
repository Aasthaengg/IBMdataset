S = input()

for alph in 'abcdefghijklmnopqrstuvwxyz':
    if alph not in S:
        print(alph)
        exit()

print('None')