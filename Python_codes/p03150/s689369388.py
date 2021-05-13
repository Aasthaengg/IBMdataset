s = input()
t = 'keyence'
if(s[:7] == t or s[-7:] == t):
    print('YES')
else:
    for i in range(7):
        if(s[:i+1] == t[:i+1] and s[-7+i+1:] == t[-7+i+1:]):
            print('YES')
            exit()
    print('NO')