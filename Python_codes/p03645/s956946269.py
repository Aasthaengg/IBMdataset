n,m = map(int,input().split())
a = [] # 1 → x
z = [] # x → n
an = 0
zn = 0
for i in range(m):
    x,y = map(int,input().split())
    if x == 1:
        zn += 1
        z.append(y)
    elif y == n:
        an += 1
        a.append(x)
    else:
        pass
a.sort()
z.sort()
i = 0
j = 0
while i < an and j < zn:
    if a[i] == z[j]:
        print('POSSIBLE')
        exit(0)
    else:
        if a[i] > z[j]:
            j += 1
        else:
            i += 1
print('IMPOSSIBLE')