N = input()
l = list()

for a in N:
    l.append(a)

if (l[0] == l[1] and l[1] == l[2]) or l[1] == l[2] and l[2] == l[3]:
    print('Yes')
else:
    print('No')