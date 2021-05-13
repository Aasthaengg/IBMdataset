s = input()
d = {'a': 0, 'b': 0, 'c': 0}

for si in s:
    d[si] += 1
d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))

value = list(d.values())
if value[0]-value[-1] > 1:
    print('NO')
else:
    print('YES')
