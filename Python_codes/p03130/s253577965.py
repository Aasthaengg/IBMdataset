#%%
a = [0] * 3
b = [0] * 3
c = []
d = [0] * 3

for i in range(3):
    a[i], b[i] = map(int, input().split())
    c.append(a[i])
    c.append(b[i])
    d[i] = ''.join(str(a[i])+str(b[i]))
    if a[i] == b[i] :
        flag = False

flag = True

if 1 <= c.count(1) <= 2 and 1 <= c.count(2) <= 2 and 1 <= c.count(3) <= 2 and 1 <= c.count(4) <= 2:
     pass
else:
    flag = False

if len(list(set(d))) == 3:
    pass
else:
    flag = False

if flag:
    print('YES')
else:
    print('NO')