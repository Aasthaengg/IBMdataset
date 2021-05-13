S = input()
n = [0] * 3
d = {'a':0, 'b':1, 'c':2}
for s in S:
    n[d[s]] += 1


if max(n) - min(n) > 1:
    print('NO')
else:
    print('YES')



