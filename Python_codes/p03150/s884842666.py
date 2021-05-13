s = input()
for i in range(8):
    b = i
    e = i+len(s)-7
    if s[:i]+s[e:]=='keyence':
        print('YES')
        break
else:
    print('NO')