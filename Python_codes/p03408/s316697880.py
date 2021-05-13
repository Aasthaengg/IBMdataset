n = int(input())
s = [str(input()) for i in range(n)]
m = int(input())
t = [str(input()) for h in range(m)]

from collections import Counter
s = Counter(s).most_common()
t = Counter(t).most_common()
l = []
for x in range(len(s)):
    z = 'Y'
    for y in range(len(t)):
        if s[x][0] == t[y][0]:
            l.append((s[x][1]-t[y][1],s[x][0]))
            z = 'N'
            break
    if z == 'Y':
        l.append((s[x][1],s[x][0]))
l.sort()
if l[-1][0] < 0:
    print(0)
else:
    print(l[-1][0])