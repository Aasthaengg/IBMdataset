line = input()

for c in line:
    if 'a' <= c <= 'z':
        print(c.upper(), end='')
    elif 'A' <= c <= 'Z':
        print(c.lower(), end='')
    else:
        print(c, end='')
print('')