# -*- coding: utf-8 -*
str = input()
for i in range(len(str)):
    if "a" <= str[i] <= "z":
        print(str[i].upper(), end='')
    else:
        print(str[i].lower(), end='')
print()