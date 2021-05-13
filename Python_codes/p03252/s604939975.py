a = {}
b = {}
i = 0
for c, d in zip(input(), input()):
    if c not in a and d not in b:
        a[c] = b[d] = i
        i += 1
    elif c in a and d in b:
        if a[c] != b[d]:
            print('No')
            break
    else:
        print('No')
        break
else:
    print('Yes')
