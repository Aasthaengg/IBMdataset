s = str(input())
z = 'YES'
while len(s) != 0:
    if s[:11] == 'dreameraser':
        s = s[11:]
    elif s[:10] == 'dreamerase':
        s = s[10:]
    elif s[:13] == 'dreamereraser':
        s = s[13:]
    elif s[:12] == 'dreamererase':
        s = s[12:]
    elif s[:7] == 'dreamer':
        s = s[7:]
    elif s[:5] == 'dream':
        s = s[5:]
    elif s[:6] == 'eraser':
        s = s[6:]
    elif s[:5] == 'erase':
        s = s[5:]
    else:
        z = 'NO'
        break
print(z)