uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowers = 'abcdefghijklmnopqrstuvwxyz'
s = str(input())
for i in range(len(s)):
    if s[i] in uppers:
        print(s[i].lower(), end='')
    elif s[i] in lowers:
        print(s[i].upper(), end='')
    else:
        print(s[i], end='')
print('')