s = input()
check = 'keyence'

if s[0] != 'k' and s[-1] != 'e':
    print('NO')
else:
    if s[:7] == check or s[-7:] == check:
        print('YES')
        exit()
    else:
        for i in range(1, 7):
            if s[:i] + s[-(7 - i):] == check:
                print('YES')
                exit()
                # print(s[:i], s[-(7 - i):])
    print('NO')
