l = [list(map(int,input().split())) for i in range(3)]
a,b = [list(i) for i in zip(*l)]
t = [0] * 4

for i in range(3):
    t[a[i] - 1] += 1
    t[b[i] - 1] += 1

if max(t) == 3:
    print('NO')
else:
    print('YES')