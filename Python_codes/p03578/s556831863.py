input()
*a, = map(int, input().split())
input()
*b, = map(int, input().split())
c = {}
d = {}
for i in a:
    c[i] = c.get(i, 0)+1
for i in b:
    d[i] = d.get(i, 0)+1
if all(c.get(i, 0) >= d[i] for i in d.keys()):
    print('YES')
else:
    print('NO')