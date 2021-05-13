s = input()
n = len(s)
l = list()
for a in range(n):
    l.append(s[a])

if len(list(set(l))) == n:
    print('yes')
else:
    print('no')
