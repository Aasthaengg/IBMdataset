s=input()
s=s[::-1]

for i in range(100000):
    if s[:5] == 'maerd':
        s = s[5:]
    if s[:5] == 'esare':
        s = s[5:]
    if s[:6] == 'resare':
        s = s[6:]
    if s[:7] == 'remaerd':
        s = s[7:]

if len(s)==0:
    print('YES')
else:
    print('NO')