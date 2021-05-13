s = str(input())

if len(s) == 1:
    print('YES')
    exit()

d = {}
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = 1
    else:
        d[s[i]] += 1
#print(d)

if len(s) == 2 and len(d) == 2:
    print('YES')
    exit()

if len(d) > 2:
    if max(d.values())-min(d.values()) <= 1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
