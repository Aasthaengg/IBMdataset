s = input()
sl = list(s)
for i in range(len(sl)):
    if (i + 1) % 2 == 1:
        if sl[i] == 'L':
            print('No')
            break
        else:
            continue
    else:
        if sl[i] == 'R':
            print('No')
            break
        else:
            continue
else:
    print('Yes')