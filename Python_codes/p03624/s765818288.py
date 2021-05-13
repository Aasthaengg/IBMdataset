n = input()
a = list('abcdefghijklmnopqrstuvwxyz')
a = set(a)
v = []
for i in a:
    if not i in n:
        v.append(i)
if len(v) == 0:
    print('None')
else:
    v.sort()
    print(v[0])