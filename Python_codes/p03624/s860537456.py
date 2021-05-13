from string import ascii_lowercase

S = input()
string = ascii_lowercase
for s in string:
    if s not in S:
        print(s)
        exit()
print('None')