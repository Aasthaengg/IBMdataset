n = input()
for c in n:
    if c == '9':
        print('1', end='')
    elif c == '1':
        print('9', end='')
    else:
        print(c, end='')
print()
