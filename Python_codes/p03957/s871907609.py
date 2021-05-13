s = input()

in_c = False

for c in s:
    if not in_c:
        if 'C' == c:
            in_c = True
    else:
        if 'F' == c:
            print('Yes')
            exit()

print('No')
