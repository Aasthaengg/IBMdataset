from string import ascii_lowercase
S = input()
for c in ascii_lowercase:
    if c not in S:
        print(c)
        exit()
print('None')
